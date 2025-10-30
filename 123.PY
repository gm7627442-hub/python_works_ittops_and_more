print('1', '2', '3', '4', '5', sep = '\n')
word1 = 'Првет, '
word2 = 'как дела'
word3 = ' чувак?'
word_all = word1 + word2 + word3
print(word_all)
print(len('academy'))
pr



# Список количества дней в месяцах (невисокосный год)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Текущая дата: 30 октября
current_day = 30
current_month = 10

# Вычисляем текущий день года (порядковый номер)
current_day_of_year = sum(days_in_month[:current_month - 1]) + current_day

# Получаем данные от пользователя
birth_day = int(input("Введите день рождения: "))
birth_month = int(input("Введите месяц рождения: "))

# Вычисляем день года для дня рождения
birth_day_of_year = sum(days_in_month[:birth_month - 1]) + birth_day

# Сравниваем с текущей датой
if birth_day_of_year > current_day_of_year:
    days_left = birth_day_of_year - current_day_of_year
else:
    # Если день рождения уже прошел, добавляем дни до конца года и дни с начала следующего года
    days_left = sum(days_in_month) - current_day_of_year + birth_day_of_year

print(f"До вашего дня рождения осталось {days_left} дней.")