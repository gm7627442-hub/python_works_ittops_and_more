#1. Задвоить элементы в списке.
# То есть компьютер превращает список [4, print, "xyz", None]
# # в список [4, 4, print, print, "xyz", "xyz", None, None]

list1 = [5, 6, 7, 8, 9, 10, 11]
max1 = len(list1)
x = 0
for i in range(max1):
    list1.insert(x, list1[x])
    x += 2
print(list1)


