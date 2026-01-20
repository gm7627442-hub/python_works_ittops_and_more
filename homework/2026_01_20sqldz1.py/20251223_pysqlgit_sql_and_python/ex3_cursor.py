from pathlib import Path
import sqlite3 as sq


BASE_DIR = Path(__file__).absolute().parent


def main():
    connection = sq.connect(BASE_DIR / "demo.db")
    
    with connection as c:
        # Получаем специальный объект ("курсор"),
        # через котороый будем давать команды
        cursor = c.cursor()

        # Через этот курсор просим выполнить
        # SQL-запрос
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS "Company"
            (
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "name" TEXT NOT NULL CHECK("name" != '')
            );
            """
        )

        # Просим "соединение" (connection) пробросить
        # набранные через execute команды в СУБД, чтобы
        # она их исполнила
        c.commit()
        
        pass


if __name__ == "__main__":
    main()