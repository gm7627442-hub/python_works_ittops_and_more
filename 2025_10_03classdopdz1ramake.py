class Fraction:
    def __init__(self, numerator, denominator):
        self.set_numerator(numerator)
        self.set_denominator(denominator)

    def get_numerator(self):
        return self.__numerator

    def set_numerator(self, value):
        self.__numerator = value

    def get_denominator(self):
        return self.__denominator

    def set_denominator(self, value):
        if value == 0:
            raise ValueError("Знаменатель не может быть нулем!")
        self.__denominator = value

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other):
        # Сложение двух дробей
        new_numerator = (
            self.__numerator * other.get_denominator()
            + other.get_numerator() * self.__denominator
        )
        new_denominator = self.__denominator * other.get_denominator()
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        # Вычитание двух дробей
        new_numerator = (
            self.__numerator * other.get_denominator()
            - other.get_numerator() * self.__denominator
        )
        new_denominator = self.__denominator * other.get_denominator()
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        # Умножение двух дробей
        new_numerator = self.__numerator * other.get_numerator()
        new_denominator = self.__denominator * other.get_denominator()
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        # Деление двух дробей
        new_numerator = self.__numerator * other.get_denominator()
        new_denominator = self.__denominator * other.get_numerator()
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        # Проверка равенства двух дробей
        return (
            self.__numerator * other.get_denominator()
            == other.get_numerator() * self.__denominator
        )

    @staticmethod
    def gcd(a, b):
        # Находим наибольший общий делитель
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        # Сокращаем дробь
        divisor = self.gcd(self.__numerator, self.__denominator)
        new_numerator = self.__numerator // divisor
        new_denominator = self.__denominator // divisor
        return Fraction(new_numerator, new_denominator)


# Если пользовотель дурачёк
a = Fraction(1, 2)  # Должно работать
print(a)

# b = Fraction(3, 0)    # Должно вызвать ошибку
# print(b)


# проверка приватности

# f = Fraction(1, 2)
# print(f.__numerator)
