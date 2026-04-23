from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Numeric,
    DateTime,
    ForeignKey,
    select,
    text,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    MappedAsDataclass,
    Mapped,
    mapped_column,
    Session,
)
from bs4 import BeautifulSoup
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from typing import Optional
import requests
import time


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Facility(Base):
    __tablename__ = "facilities"

    facid: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    membercost: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    guestcost: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    initialoutlay: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    monthlymaintenance: Mapped[Decimal] = mapped_column(Numeric(10, 2))


class Member(Base):
    __tablename__ = "members"

    memid: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String(200))
    firstname: Mapped[str] = mapped_column(String(200))
    address: Mapped[str] = mapped_column(String(300))
    zipcode: Mapped[int] = mapped_column(Integer)
    telephone: Mapped[str] = mapped_column(String(20))
    recommendedby: Mapped[Optional[int]] = mapped_column(
        ForeignKey("members.memid"),
        nullable=True,
    )
    joindate: Mapped[datetime] = mapped_column(DateTime)


class Booking(Base):
    __tablename__ = "bookings"

    bookid: Mapped[int] = mapped_column(Integer, primary_key=True)
    facid: Mapped[int] = mapped_column(ForeignKey("facilities.facid"))
    memid: Mapped[int] = mapped_column(ForeignKey("members.memid"))
    starttime: Mapped[datetime] = mapped_column(DateTime)
    slots: Mapped[int] = mapped_column(Integer)


engine = create_engine("sqlite:///club.db", echo=False)
Base.metadata.create_all(engine)

base_dir = Path(__file__).parent

facilities_file = base_dir / "cd.facilitespars.txt"
members_file = base_dir / "cd.members.txt"
bookings_file = base_dir / "cd.bookingspars.txt"


def read_html_file(file_path: Path) -> BeautifulSoup:
    with open(file_path, "r", encoding="utf-8") as file:
        return BeautifulSoup(file.read(), "html.parser")


def parse_facilities(file_path: Path):
    soup = read_html_file(file_path)
    rows = soup.find("tbody").find_all("tr")
    facilities = []

    for row in rows:
        cols = row.find_all("td")
        facility = Facility(
            facid=int(cols[0].text.strip()),
            name=cols[1].text.strip(),
            membercost=Decimal(cols[2].text.strip()),
            guestcost=Decimal(cols[3].text.strip()),
            initialoutlay=Decimal(cols[4].text.strip()),
            monthlymaintenance=Decimal(cols[5].text.strip()),
        )
        facilities.append(facility)

    return facilities


def parse_members(file_path: Path):
    soup = read_html_file(file_path)
    rows = soup.find("tbody").find_all("tr")
    members = []

    for row in rows:
        cols = row.find_all("td")
        rec = cols[6].text.strip()
        rec_value = int(rec) if rec else None

        member = Member(
            memid=int(cols[0].text.strip()),
            surname=cols[1].text.strip(),
            firstname=cols[2].text.strip(),
            address=cols[3].text.strip(),
            zipcode=int(cols[4].text.strip()),
            telephone=cols[5].text.strip(),
            recommendedby=rec_value,
            joindate=datetime.strptime(cols[7].text.strip(), "%Y-%m-%d %H:%M:%S"),
        )
        members.append(member)

    return members


def parse_bookings(file_path: Path):
    soup = read_html_file(file_path)
    rows = soup.find("tbody").find_all("tr")
    bookings = []

    for row in rows:
        cols = row.find_all("td")
        booking = Booking(
            bookid=int(cols[0].text.strip()),
            facid=int(cols[1].text.strip()),
            memid=int(cols[2].text.strip()),
            starttime=datetime.strptime(cols[3].text.strip(), "%Y-%m-%d %H:%M:%S"),
            slots=int(cols[4].text.strip()),
        )
        bookings.append(booking)

    return bookings


def load_data():
    facilities = parse_facilities(facilities_file)
    members = parse_members(members_file)
    bookings = parse_bookings(bookings_file)

    with Session(engine) as session:
        session.query(Booking).delete()
        session.query(Member).delete()
        session.query(Facility).delete()
        session.commit()

        session.add_all(facilities)
        session.add_all(members)
        session.add_all(bookings)
        session.commit()


def print_rows(rows):
    for row in rows:
        print(row)


def save_to_file(rows):
    with open("result.txt", "w", encoding="utf-8") as file:
        for row in rows:
            file.write(str(row) + "\n")
    print("Результат сохранен в result.txt")


def normalize_value(value):
    if isinstance(value, Decimal):
        return float(value)

    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")

    if value is None:
        return ""

    return str(value).strip()


def normalize_user_rows(rows):
    result = []

    for row in rows:
        if hasattr(row, "_mapping"):
            values = list(row._mapping.values())
        else:
            values = list(row)

        normalized_row = []
        for value in values:
            normalized_row.append(normalize_value(value))

        result.append(normalized_row)

    return result


def split_expected_line(line):
    parts = line.split()
    return [part.strip() for part in parts]

def load_tasks_from_site():
    base_url = "https://pgexercises.com/questions"
    categories = [
        "basic",
        "joins",
        "updates",
        "aggregate",
        "date",
        "string",
        "recursive"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    all_links = []

    for category in categories:
        url = f"{base_url}/{category}/"

        try:
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, "html.parser")

            links = soup.find_all("a")

            for link in links:
                href = link.get("href")

                if href and href.endswith(".html") and "/" not in href:
                    full_link = f"{base_url}/{category}/{href}"

                    if full_link not in all_links:
                        all_links.append(full_link)

            print("Категория собрана:", category)

        except requests.exceptions.RequestException as e:
            print("Ошибка при открытии категории:", category)
            print(e)

    all_tasks = []

    for link in all_links:
        try:
            response = requests.get(link, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, "html.parser")

            title = ""
            question = ""
            expected_headers = []
            expected_rows = []

            h1 = soup.find("h1")
            if h1:
                title = h1.get_text(" ", strip=True)

            h3_list = soup.find_all("h3")

            for h3 in h3_list:
                h3_text = h3.get_text(" ", strip=True)

                if "Question" in h3_text:
                    question_parts = []
                    current = h3.find_next_sibling()

                    while current:
                        if current.name == "h3":
                            break

                        text_value = current.get_text(" ", strip=True)
                        if text_value and "Schema reminder" not in text_value:
                            question_parts.append(text_value)

                        current = current.find_next_sibling()

                    question = " ".join(question_parts)

                if "Expected Results" in h3_text:
                    current = h3.find_next_sibling()

                    while current:
                        if current.name == "h3":
                            break

                        table = current.find("table") if current else None

                        if current.name == "table":
                            table = current

                        if table:
                            rows = table.find_all("tr")

                            if rows:
                                first_row_cells = rows[0].find_all(["th", "td"])
                                expected_headers = [
                                    cell.get_text(" ", strip=True)
                                    for cell in first_row_cells
                                ]

                                for row in rows[1:]:
                                    cells = row.find_all(["th", "td"])
                                    row_data = [
                                        cell.get_text(" ", strip=True)
                                        for cell in cells
                                    ]

                                    if row_data:
                                        expected_rows.append(row_data)

                            break

                        current = current.find_next_sibling()

            task_data = {
                "link": link,
                "title": title,
                "question": question,
                "headers": expected_headers,
                "expected_rows": expected_rows,
            }

            all_tasks.append(task_data)
            print("Собрано задание:", title)

            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print("Ошибка при открытии задания:", link)
            print(e)

    return all_tasks

def run_orm():
    print("Пример ORM запроса:")
    print("select(Facility.name).where(Facility.membercost > 0)")
    orm_query = input("Введи ORM запрос: ")

    try:
        stmt = eval(orm_query)
        with Session(engine) as session:
            rows = session.execute(stmt).fetchall()
        return rows
    except Exception as e:
        print("Ошибка:", e)
        return []


def run_sql():
    print("Пример SQL запроса:")
    print("SELECT name FROM facilities WHERE membercost > 0;")
    sql_query = input("Введи SQL запрос: ")

    try:
        with Session(engine) as session:
            rows = session.execute(text(sql_query)).fetchall()
        return rows
    except Exception as e:
        print("Ошибка:", e)
        return []


def compare_results(user_rows, correct_rows):
    user_normalized = normalize_user_rows(user_rows)

    if user_normalized == correct_rows:
        print("Ответ правильный")
    else:
        print("Ответ неправильный")
        print("Твой результат:")
        for row in user_normalized:
            print(row)

        print("Правильный ответ:")
        for row in correct_rows:
            print(row)


def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i} - {task['title']}")


def solve_task(tasks):
    if not tasks:
        print("Список задач пуст")
        return

    print("Выбери задачу:")
    show_tasks(tasks)

    try:
        task_number = int(input("Номер задачи: "))
    except ValueError:
        print("Нужно ввести число")
        return

    if task_number < 1 or task_number > len(tasks):
        print("Неверный номер задачи")
        return

    task = tasks[task_number - 1]
    print("\nНазвание:")
    print(task["title"])

    print("\nВопрос:")
    print(task["question"])

    print("\nОжидаемый результат:")

    if task["headers"]:
        print(" | ".join(task["headers"]))
        print("-" * 100)

    for row in task["expected_rows"]:
        print(" | ".join(row))

    print("\nВыбери способ решения:")
    print("1 - ORM")
    print("2 - SQL")

    method = input("Твой выбор: ")

    if method == "1":
        user_rows = run_orm()
    elif method == "2":
        user_rows = run_sql()
    else:
        print("Неверный выбор")
        return

    compare_results(user_rows, task["expected_rows"])

    save = input("Сохранить результат в файл? (y/n): ")
    if save.lower() == "y":
        save_to_file(user_rows)


def main():
    tasks = []

    while True:
        print("\nМеню:")
        print("1 - Загрузить данные в БД")
        print("2 - Загрузить задания с сайта")
        print("3 - Решить задачу")
        print("4 - Выход")

        choice = input("Выбери пункт: ")

        if choice == "1":
            load_data()
            print("Данные загружены")

        elif choice == "2":
            tasks = load_tasks_from_site()
            print("Задания загружены:", len(tasks))

        elif choice == "3":
            solve_task(tasks)

        elif choice == "4":
            print("Программа завершена")
            break

        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()