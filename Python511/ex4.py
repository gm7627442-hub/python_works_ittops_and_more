# Удаление элемента с конца списка
things = [print, None, True, 5, "dfd", str]
print("\nДо удаления:\n", things)

popped_element = things.pop()
print("\nПосле использования pop:\n", things)
print("\nБыл вытолкнут элемент: ", popped_element)

# `pop` - это обратное действие к `append`
