from pathlib import Path
import sqlite3 as sq


BASE_DIR = Path(__file__).absolute().parent


def create_tables(connection: sq.Connection) -> bool:

    is_complete = False

    # Получаем специальный объект ("курсор"),
    # через котороый будем давать команды
    cursor = connection.cursor()

    try:
        # Через этот курсор просим выполнить
        # SQL-запрос
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS "Company"
            (
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "name" TEXT NOT NULL CHECK("name" != '') UNIQUE,
                "owner" TEXT NOT NULL CHECK("name" != '')
            );
            """
        )

        # Просим "соединение" (connection) пробросить
        # набранные через execute команды в СУБД, чтобы
        # она их исполнила
        connection.commit()

        is_complete = True
    
    except sq.Error as error:
        print(f"create_tables(): Ошибка:\n\t{error}\n")

    return is_complete


def populate_tables(connection: sq.Connection) -> bool:

    is_complete = False
    cursor = connection.cursor()

    company_names = [
        ("Yandex", "Ягода Михаил Потапович"),
        ("MatroskinCo", "Кот Матроскин"),
    ]

    try:
        cursor.executemany(
            """
            INSERT INTO "Company"
                ("name", "owner")
            VALUES
                (?, ?)
            """,
            company_names
        )
        connection.commit()

        is_complete = True

    except sq.Error as error:
        print(f"populate_tables(): Ошибка:\n\t{error}\n")
    
    return is_complete


def use_database(connection: sq.Connection) -> None:

    with connection as active_connection:
        print("Таблицы создаются...")
        is_tables_creation_complete = create_tables(active_connection)

        if not is_tables_creation_complete:
            return
        
        print("Таблицы созданы!")
            
        print("Таблицы наполняются данными...")
        is_tables_population_complete = populate_tables(active_connection)

        if not is_tables_population_complete:
            return
        
        print("Таблицы наполнены данными!")


def main():
    connection = sq.connect(BASE_DIR / "demo.db")
    use_database(connection)


if __name__ == "__main__":
    main()