things = [3, "dddd", None]
elements = things  # Это. Не. Копирование. Списка. Это создание псевдонима

print("things =", things)
print(f"{elements = }")  # краткая версия print на строке 4
print()

elements.append(7777)  # Это "повлияет" и на things

print(f"{things = }")
print(f"{elements = }")
print()

# things и elements хранят ссылка на данные (объект)