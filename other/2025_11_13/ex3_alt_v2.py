# Удаление по значению всех вхождений элементов
things = [print, None, True, 5, "dfd", str, True]
print("\nДо удаления:\n", things)

element_for_delete = True

for index, element in enumerate(things):
    if element == element_for_delete:
        del things[index]

print("\nПосле использования del в цикле:\n", things)
