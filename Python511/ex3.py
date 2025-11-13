# Удаление элемента по значение (то есть
# мы знаем, что это за элемент, но не знаем
# его индекса)
things = [print, None, True, 5, "dfd", str, True]
print("\nДо удаления:\n", things)

things.remove(True)  # Удалит первое вхождение (слева)
print("\nПосле использования remove:\n", things)
