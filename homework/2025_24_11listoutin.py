n = int(input("Сколько целых чисел надо положить в список? "))


if n <= 0:
    original_list = []
else:
    original_list = []
    for i in range(n):
        num = int(input(f"Введите число {i + 1}: "))
        original_list.append(num)

result_list = []
for num in original_list:
    if num > 0:
        result_list.append([num] * num)
    else:
        result_list.append([])

print("\nИсходный список:")
print(original_list)
print("\nРезультирующий список списков:")
print("[")
for i, sublist in enumerate(result_list):
    # Форматируем вывод каждого подсписка
    if i == len(result_list) - 1:  # Последний элемент без запятой
        print(f"    {sublist}")
    else:
        print(f"    {sublist},")
print("]")
