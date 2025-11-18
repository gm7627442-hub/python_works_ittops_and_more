ROW_COUNT = 10

table = []

for _ in range(ROW_COUNT):
    table.append([])  # Здесь создаётся на каждом ветке цикла новый пустой список

print(table)

table[0].append(1)
print(table)