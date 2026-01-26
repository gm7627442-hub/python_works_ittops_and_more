import sqlite3 as sq


def main():
    connection = sq.connect("demo.db")
    
    with connection as c:
        pass


if __name__ == "__main__":
    main()