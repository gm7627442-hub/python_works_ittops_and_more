ROW_COUNT = 10

generator = ([] for _ in range(ROW_COUNT))  # генераторное выражение; в данном случае порождает генератор списков
print(generator)
table = list(generator)
print(table)

table[0].append(1)
print(table)