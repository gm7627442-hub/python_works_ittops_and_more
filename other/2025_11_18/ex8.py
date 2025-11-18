# Создать список квадратов целых чисел от -3 до 7,
# который хранит только чётные значения

numbers = [x * x for x in range(-3, 7 + 1) if x % 2 == 0]
print(numbers)

# Более читаемый вариант (на мой взгляд)
numbers = [
    x * x
    for x in range(-3, 7 + 1)
    if x % 2 == 0
]
print(numbers)


