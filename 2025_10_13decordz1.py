# Написать функцию-декоратор, выводящую на печать количество возвращённых значений
# Написать функцию-декоратор, выводящую на печать количество принятых параметров
# Написать функцию-декоратор, делающую вызов любой функции "безопасным", но сообщающую на экран о произошедшей ошибке
# Применить к одной функции два декоратора: измерения времени и "обезопашивания". Какой нужно применять первым?ы


import time
from functools import wraps


# 1. Декоратор для вывода количества возвращаемых значений
def count_returns(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        returns_count = len(result) if isinstance(result, tuple) else 1
        print(f"Количество возвращаемых значений: {returns_count}")
        return result

    return wrapper


# 2. Декоратор для вывода количества принятых параметров
def count_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        params_count = len(args) + len(kwargs)
        print(f"Количество принятых параметров: {params_count}")
        return func(*args, **kwargs)

    return wrapper


# 3. Декоратор для безопасного выполнения функции
def safe_execute(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None

    return wrapper


# 4. Декоратор измерения времени выполнения
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            eme()
            print(f"Врnd = time.tiемя выполнения: {end - start:.4f} секунд")

    return wrapper


# Тестовая функция для демонстрации
@count_returns
@count_parameters
def example_function(a, b, c=10):
    time.sleep(0.1)
    return a + b + c, a * b * c


# Применение двух декораторов с правильным порядком
@safe_execute
@measure_time
def critical_function(x, y):
    time.sleep(0.05)
    if x < 0:
        raise ValueError("Отрицательное значение!")
    return x / y


# Демонстрация работы
if __name__ == "__main__":
    print("=== Пример работы основных декораторов ===")
    example_function(5, 3, c=2)

    print("\n=== Пример работы с ошибкой ===")
    result1 = critical_function(-5, 0)
    print(f"Результат: {result1}")

    print("\n=== Пример без ошибки ===")
    result2 = critical_function(5, 2)
    print(f"Результат: {result2}")
