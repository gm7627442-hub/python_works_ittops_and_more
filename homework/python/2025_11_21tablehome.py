import random

height = random.randint(0, 10)
width = random.randint(0, 10)
table = [[random.randint(-10, 10) for _ in range(width)] for _ in range(height)]

while True:
    print("Текущее состояние таблицы:")
    if not table:
        print("Таблица пуста")
    else:
        for row in table:
            print(' '.join(f'{val:3}' for val in row))
    print()
    
    print("1 - поменять местами строки")
    print("2 - поменять местами столбцы") 
    print("0 - выйти")
    
    choice = input(">>> ").strip()
    
    if choice == '0':
        break
    elif choice == '1':
        if len(table) == 0:
            print("Таблица пуста, операция невозможна\n")
            continue
            
        print(f"Доступно строк: {len(table)}")
        
        while True:
            try:
                i1 = int(input("Первый индекс строки: "))
                if 0 <= i1 < len(table):
                    break
                print(f"Индекс должен быть от 0 до {len(table)-1}")
            except ValueError:
                print("Введите целое число")
        
        while True:
            try:
                i2 = int(input("Второй индекс строки: "))
                if 0 <= i2 < len(table):
                    break
                print(f"Индекс должен быть от 0 до {len(table)-1}")
            except ValueError:
                print("Введите целое число")
        
        table[i1], table[i2] = table[i2], table[i1]
        print("Строки поменяны местами\n")
        
    elif choice == '2':
        if len(table) == 0 or len(table[0]) == 0:
            print("Таблица пуста или нет столбцов, операция невозможна\n")
            continue
            
        print(f"Доступно столбцов: {len(table[0])}")
        
        while True:
            try:
                i1 = int(input("Первый индекс столбца: "))
                if 0 <= i1 < len(table[0]):
                    break
                print(f"Индекс должен быть от 0 до {len(table[0])-1}")
            except ValueError:
                print("Введите целое число")
        
        while True:
            try:
                i2 = int(input("Второй индекс столбца: "))
                if 0 <= i2 < len(table[0]):
                    break
                print(f"Индекс должен быть от 0 до {len(table[0])-1}")
            except ValueError:
                print("Введите целое число")
        
        for row in table:
            row[i1], row[i2] = row[i2], row[i1]
        print("Столбцы поменяны местами\n")
        
    else:
        print("Неверный ввод. Выберите 0, 1 или 2\n")