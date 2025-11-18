# Вставка ("вклинивание") элемента в произвольную
# позицию (т. е. индекс) в списке
things = [print, None, True, 5, "dfd", str]
print("\nДо вставки:\n", things)

things.insert(1, "*****")
print("\nПосле вставки (insert):\n", things)

things.insert(10000, "++++")  # Будет работать как append 
print("\nПосле вставки (insert):\n", things)
