employees = []
rooms = []
assignments = {}
error_msg = ""

print("Система 'Привязь' запущена")

while True:
    print("\n" + "="*50)
    print("Система 'Привязь' - Учет кабинетов")
    
    if assignments:
        print("\nАктивные связи:")
        for emp, room in assignments.items():
            print(f"  {emp} - {room}")
    else:
        print("\nАктивных связей нет")
    
    if error_msg:
        print(f"\n{error_msg}")
        error_msg = ""
    
    
    print("\nГлавное меню:")
    print("1 - Связать сотрудника и кабинет")
    print("2 - Отвязать сотрудника от кабинета")
    print("3 - Добавить сотрудника")
    print("4 - Удалить сотрудника")
    print("5 - Добавить кабинет")
    print("6 - Удалить кабинет")
    print("0 - Выйти из системы")
    
    choice = input("\nВыберите действие: ").strip()
    
    if choice == "0":
        print("\nВыход из системы...")
        break
    
    elif choice == "1":
        if not employees or not rooms:
            error_msg = "Нет сотрудников и/или комнат."
            continue
        
        free_employees = [e for e in employees if e not in assignments]
        if not free_employees:
            error_msg = "Все сотрудники уже привязаны к кабинетам!"
            continue
        
        print("\n" + "="*50)
        print("Выбор сотрудника для привязки:")
        for i, emp in enumerate(free_employees, 1):
            print(f"{i}. {emp}")
        print("0. Отмена")
        
        try:
            emp_num = int(input("\nНомер сотрудника: "))
            if emp_num == 0:
                continue
            emp_selected = free_employees[emp_num-1]
        except:
            error_msg = "Ошибка: данные указнны не верно попробуйте ещё раз!"
            continue
        
        occupied_rooms = [room for room in assignments.values()]
        free_rooms = [room for room in rooms if room not in occupied_rooms]
        
        if not free_rooms:
            error_msg = "Нет свободных кабинетов!"
            continue
        
        print("\n" + "="*50)
        print(f"Выбор кабинета для сотрудника: {emp_selected}")
        for i, room in enumerate(free_rooms, 1):
            print(f"{i}. {room}")
        print("0. Отмена")
        
        try:
            room_num = int(input("\nНомер кабинета: "))
            if room_num == 0:
                continue
            room_selected = free_rooms[room_num-1]
        except:
            error_msg = "Ошибка: данные указнны не верно попробуйте ещё раз!"
            continue
        
        old_room = assignments.get(emp_selected)
        assignments[emp_selected] = room_selected
        error_msg = f"Связь {'обновлена' if old_room else 'создана'}: {emp_selected} - {room_selected}"
        if old_room:
            error_msg += f" (был в {old_room})"
    
    elif choice == "2":
        if not assignments:
            error_msg = "Нет активных связей!"
            continue
        
        print("\n" + "="*50)
        print("Отвязка сотрудника:")
        items = list(assignments.items())
        for i, (emp, room) in enumerate(items, 1):
            print(f"{i}. {emp} - {room}")
        print("0. Отмена")
        
        try:
            link_num = int(input("\nНомер связи для отвязки: "))
            if link_num == 0:
                continue
            emp_to_remove, room_to_remove = items[link_num-1]
        except:
            error_msg = "Ошибка: данные указнны не верно попробуйте ещё раз!."
            continue
        
        del assignments[emp_to_remove]
        error_msg = f"Сотрудник {emp_to_remove} отвязан от кабинета {room_to_remove}"
    
    elif choice == "3":
        print("\n" + "="*50)
        print("Добавление нового сотрудника\n(оставьте пустым для отмены)")
        name = input("\nВведите ФИО сотрудника: ").strip()
        
        if not name:
            error_msg = "Добавление отменено."
        elif name in employees:
            error_msg = f"Сотрудник '{name}' уже существует!"
        else:
            employees.append(name)
            error_msg = f"Сотрудник '{name}' успешно добавлен!"
    
    elif choice == "4":
        if not employees:
            error_msg = "Список сотрудников пуст!"
            continue
        
        print("\n" + "="*50)
        print("Удаление сотрудника:")
        for i, emp in enumerate(employees, 1):
            print(f"{i}. {emp}{' (привязан)' if emp in assignments else ''}")
        print("0. Отмена")
        
        try:
            emp_num = int(input("\nНомер сотрудника для удаления: "))
            if emp_num == 0:
                continue
            emp_to_delete = employees[emp_num-1]
        except:
            error_msg = "Ошибка: данные указнны не верно попробуйте ещё раз!."
            continue
        
        if emp_to_delete in assignments:
            del assignments[emp_to_delete]
        employees.remove(emp_to_delete)
        error_msg = f"Сотрудник '{emp_to_delete}' удален!"
    
    elif choice == "5":
        print("\n" + "="*50)
        print("Добавление нового кабинета\n(оставьте пустым для отмены)")
        name = input("\nВведите название кабинета: ").strip()
        
        if not name:
            error_msg = "Добавление отменено."
        elif name in rooms:
            error_msg = f"Кабинет '{name}' уже существует!"
        else:
            rooms.append(name)
            error_msg = f"Кабинет '{name}' успешно добавлен!"
    
    elif choice == "6":
        if not rooms:
            error_msg = "Список кабинетов пуст!"
            continue
        
        print("\n" + "="*50)
        print("Удаление кабинета:")
        for i, room in enumerate(rooms, 1):
            occupied = any(room == rm for emp, rm in assignments.items())
            print(f"{i}. {room}{' (занят)' if occupied else ''}")
        print("0. Отмена")
        
        try:
            room_num = int(input("\nНомер кабинета для удаления: "))
            if room_num == 0:
                continue
            room_to_delete = rooms[room_num-1]
        except:
            error_msg = "Ошибка: данные указнны не верно попробуйте ещё раз!."
            continue
        
        to_remove = [emp for emp, room in assignments.items() if room == room_to_delete]
        for emp in to_remove:
            del assignments[emp]
        
        rooms.remove(room_to_delete)
        removed = len(to_remove)
        error_msg = f"Кабинет '{room_to_delete}' удален{f'! Отвязано сотрудников: {removed}' if removed else '!'}"
    
    else:
        error_msg = "Неверный выбор! Введите число от 0 до 6."