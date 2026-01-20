from pathlib import Path
import sqlite3 as sq

BASE_DIR = Path(__file__).absolute().parent

def create_tables(connection: sq.Connection) -> bool:
    is_complete = False
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS "Plants"
            (
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "name" TEXT NOT NULL CHECK("name" != '') UNIQUE,
                "room" TEXT NOT NULL CHECK("room" != ''),
                "responsible_person" TEXT NOT NULL CHECK("responsible_person" != '')
            );
            """
        )
        connection.commit()
        is_complete = True

    except sq.Error as error:
        print(f"create_tables(): Ошибка:\n\t{error}\n")

return is_complete

def populate_tables(connection: sq.Connection) -> bool:
    is_complite = False
    Cursor = connection.cursor()
    
    try:
        try:
            count = int(input("Сколько растений вы хотите внести в БД?"))
            if count <= 0:
                print("числодолжно быть целым ")
                return False
        except ValueError:
            print("Пожалуйста введите целое число")
            return False

        plants_data = []
        
        print("\nВведите данные для каждого растения:")
        for i in range(1, count + 1):
            print(f"\nРастение #{i}:")
            
            name = input("Название растения: ").strip()
            while not name:
                print("Название не может быть пустым!")
                name = input("Название растения: ").strip()
            
            room = input("Комната (где стоит растение): ").strip()
            while not room:
                print("Комната не может быть пустой!")
                room = input("Комната (где стоит растение): ").strip()
            
            responsible = input("ФИО ответственного за полив: ").strip()
            while not responsible:
                print("ФИО не может быть пустым!")
                responsible = input("ФИО ответственного за полив: ").strip()
            
            plants_data.append((name, room, responsible))
            
        cursor.executemany(
            """
            INSERT INTO "Plants"
                (name, room, responsible_person)
            VAlUES 
                (?, ?, ?)
            """,
            plants_data
        )
        connetcion.commit()
        
        print(f"\nУспешно добавлено {len(plants_data)} растений!")
        s_complete = True
        
    except sq.Error as error:
        print(f"populate_tables(): Ошибка:\n\t{error}\n")
        
return is_complete
