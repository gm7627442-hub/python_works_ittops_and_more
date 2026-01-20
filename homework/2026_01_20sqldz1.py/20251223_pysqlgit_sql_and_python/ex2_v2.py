from pathlib import Path
import sqlite3 as sq


BASE_DIR = Path(__file__).absolute().parent


def main():
    connection = sq.connect(BASE_DIR / "demo.db")
    
    with connection as c:
        pass


if __name__ == "__main__":
    main()