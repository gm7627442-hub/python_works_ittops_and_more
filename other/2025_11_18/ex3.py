numbers = [3, 5, -2, 1]

table = []
table.append(numbers[:])  # Копия через срез
table.append(numbers[:])
table.append(numbers[:])
print(f"{table = }")

numbers.append("xyz")
table[0].append("AAA")
table[1].append("BBB")
table[2].append("CCC")
print(f"{table = }")  # Да, тут table
