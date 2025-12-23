# Получить математический пример с клавиатуры, вычеслить!


print("Простой калькулятор")
print("Доступные операции: +, -, *, /")
print("Для выхода введите 'exit'")

while True:
    try:
        # Ввод данных
        user_input = input("Введите выражение: ").strip()
        if user_input.lower() == 'exit':
            break

        # Поиск оператора
        operator = None
        for op in ['+', '-', '*', '/']:
            if op in user_input:
                operator = op
                break

        if not operator:
            print("Ошибка: оператор не найден")
            continue

        # Разделение на числа
        parts = user_input.split(operator)
        if len(parts) != 2:
            print("Ошибка: неверный формат ввода")
            continue

        a = float(parts[0].strip())
        b = float(parts[1].strip())

        # Вычисления
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                print("Ошибка: деление на ноль")
                continue
            result = a / b

        # Вывод результата
        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: введите числа корректно")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

print("Работа калькулятора завершена")