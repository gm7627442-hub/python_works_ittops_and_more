class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулем!")

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        # Сложение двух дробей
        new_numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        # Вычитание двух дробей
        new_numerator = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        # Умножение двух дробей
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        # Деление двух дробей
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        # Проверка равенства двух дробей
        return self.numerator * other.denominator == other.numerator * self.denominator

    def gcd(self, a, b):
        # Находим наибольший общий делитель
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        # Сокращаем дробь
        divisor = self.gcd(self.numerator, self.denominator)
        new_numerator = self.numerator // divisor
        new_denominator = self.denominator // divisor
        return Fraction(new_numerator, new_denominator)


# Если пользовотель дурачёк
a = Fraction(1, 2)  # Должно работать
print(a)

# b = Fraction(3, 0)    # Должно вызвать ошибку
# print(b)
