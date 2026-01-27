from pathlib import Path
import sqlite3 as sq


BASE_DIR = Path(__file__).absolute().parent


def create_tables(connection: sq.Connection) -> bool:
    is_complete = False
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS "Flower"
            (
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "name" TEXT NOT NULL CHECK("name" != ''),
                "room" TEXT NOT NULL CHECK("room" != ''),
                "responsible" TEXT NOT NULL CHECK("responsible" != '')
            );
            """
        )

        connection.commit()
        is_complete = True

    except sq.Error as error:
        print(f"create_tables(): Ошибка:\n\t{error}\n")

    return is_complete


def populate_tables(connection: sq.Connection) -> bool:
    is_complete = False
    cursor = connection.cursor()

    try:
        count = int(input("Сколько растений вы хотите добавить? "))

        flowers = []

        for i in range(count):
            print(f"\nРастение №{i + 1}")
            name = input("Название растения: ").strip()
            room = input("Комната: ").strip()
            responsible = input("ФИО ответственного за полив: ").strip()

            flowers.append((name, room, responsible))

        cursor.executemany(
            """
            INSERT INTO "Flower"
                ("name", "room", "responsible")
            VALUES
                (?, ?, ?)
            """,
            flowers
        )

        connection.commit()
        is_complete = True

    except ValueError:
        print("Ошибка: количество растений должно быть числом.")
    except sq.Error as error:
        print(f"populate_tables(): Ошибка:\n\t{error}\n")

    return is_complete


def use_database(connection: sq.Connection) -> None:
    with connection as active_connection:
        print("Таблицы создаются...")
        if not create_tables(active_connection):
            return
        print("Таблицы созданы!")

        print("Таблицы наполняются данными...")
        if not populate_tables(active_connection):
            return
        print("Таблицы наполнены данными!")


def main():
    connection = sq.connect(BASE_DIR / "flowers.db")
    use_database(connection)


if __name__ == "__main__":
    main()
