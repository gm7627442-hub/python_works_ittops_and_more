import dataclasses


# "Описание" комплекта из трёх переменных
@dataclasses.dataclass
class Birka:
    id: int
    text: str
    author: str


# Создание конкретных экземпляров класса
zapiska_1 = Birka(id=12, text="Помыть кота", author="я")
zapiska_2 = Birka(1, "Зарплата!", "не я")
print(zapiska_1)
print(zapiska_1.id, zapiska_1.text, zapiska_1.author)
print(zapiska_2)


# Здесь класс - это модель бирки; в данной модели
# нам не нужно знать, например, из какого материала
# бирка (задача этого не треюбует)


# В БД таблица - это как бы класс, а запись
# в таблице - это как бы экземпляр класса.
# Столбцы - атрибуты (поля). (id, text, author)