# Есть набор литер: "А", "Б" и "В".
# Для каждой литеры есть 4 посадочных места.
# Создать список бирок для каждого посадочного
# места (все возжмодные комбинации пар)

liters = ["А", "Б", "В"]
seat_numbers = range(4)

labels = [
    f"{liter}{seat_number + 1}"
    for liter in liters
    for seat_number in seat_numbers    
]
print(labels)