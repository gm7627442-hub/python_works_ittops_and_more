from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Numeric,
    DateTime,
    ForeignKey,
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


engine = create_engine("sqlite:///club.db", echo=True)
Base.metadata.create_all(engine)

base_dir = Path(__file__).parent

facilities_file = base_dir / "cd.facilitespars.txt"
members_file = base_dir / "cd.members.txt"
bookings_file = base_dir / "cd.bookingspars.txt"


def read_html_file(file_path: Path) -> BeautifulSoup:
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()
    return BeautifulSoup(html, "html.parser")


def parse_facilities(file_path: Path) -> list[Facility]:
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


def parse_members(file_path: Path) -> list[Member]:
    soup = read_html_file(file_path)
    rows = soup.find("tbody").find_all("tr")
    members = []
    for row in rows:
        cols = row.find_all("td")
        recommended_text = cols[6].text.strip()
        recommended_value = int(recommended_text) if recommended_text else None
        member = Member(
            memid=int(cols[0].text.strip()),
            surname=cols[1].text.strip(),
            firstname=cols[2].text.strip(),
            address=cols[3].text.strip(),
            zipcode=int(cols[4].text.strip()),
            telephone=cols[5].text.strip(),
            recommendedby=recommended_value,
            joindate=datetime.strptime(
                cols[7].text.strip(),
                "%Y-%m-%d %H:%M:%S",
            ),
        )
        members.append(member)
    return members


def parse_bookings(file_path: Path) -> list[Booking]:
    soup = read_html_file(file_path)
    rows = soup.find("tbody").find_all("tr")
    bookings = []
    for row in rows:
        cols = row.find_all("td")
        booking = Booking(
            bookid=int(cols[0].text.strip()),
            facid=int(cols[1].text.strip()),
            memid=int(cols[2].text.strip()),
            starttime=datetime.strptime(
                cols[3].text.strip(),
                "%Y-%m-%d %H:%M:%S",
            ),
            slots=int(cols[4].text.strip()),
        )
        bookings.append(booking)
    return bookings


facilities = parse_facilities(facilities_file)
members = parse_members(members_file)
bookings = parse_bookings(bookings_file)

with Session(engine) as session:
    session.query(Booking).delete()
    session.query(Member).delete()
    session.query(Facility).delete()
    session.commit()

    session.add_all(facilities)
    session.commit()

    session.add_all(members)
    session.commit()

    session.add_all(bookings)
    session.commit()

print("Все данные успешно добавлены")