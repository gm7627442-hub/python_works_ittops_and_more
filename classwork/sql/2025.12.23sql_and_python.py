from pathlib import Path
import sqlite3 as sq 


BASE_DIR = Path(__file__).absolute().parent

def create_tables(connection: sq.connect):
    is_complite = False
    
    cursor = connection.cursor()
    
    try:
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS "Company"
            (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "name" TEXT NOT NULL CHECK("name" <> '') UNIQUE,
            "owner" TEXT NOT NULL CHECK("owner" <> '')
            );
        """
        )
            
        connection.commit()
    
        is_complite = True
    
    except sq.Error as error:
        print(f"Ошибка:\n\t{error}\n")

    return is_complite

def populate_tables(connection: sq.connect):
    
    is_complite = False
    cursor = connection.cursor()
    
    company_names = [
        ("Yandex", "Ценов Натакси Зоблачны"),
        ("Dota2", "Гейб Нювелл"),
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
        
        is_complite = True
        
    except sq.Error as error:
        print(f"populate_tabel():Ошибка:\n\t{error}\n")
    
    return is_complite
     

def main():
    connection = sq.connect(BASE_DIR / "demo.db")
    
    with connection as active_connection:
       is_table_creation_complite = create_tables(active_connection)
       
       if is_table_creation_complite:
           print("Таблицы созданы")
           
           is_table_population_complite = populate_tables(active_connection)
           
           if is_table_population_complite:
               print('Таблицы созданы')

    
     

if __name__ == "__main__":
    main() 
    
