# Написать программу, которая спрашивает 
# у пользователя целое количество часов и выводит 
# количество часов до сна (23:00) Пример работы:

ask = input('Который час? (укажите целое число): ')
ask = int(ask)
if ask <0 and ask > 23:
    raise ValueError('Вы указали не возможно время')
elif ask == 0:
    print('Вы опазадали')
    exit()
elif ask == 23:
    print('Пора спать!')
    exit()

time_sleep = 23

print("До сна соталось часа(-ов)", time_sleep - ask)


# Задача №2
# Написать программу, которая спрашивает у пользователя, который час и выводит в ответ время суток. Границы определить любые, но в каждом времени суток должно быть непустое количество часов. Пример работы программы:
# Программа: Который час?
# Пользователь: 19:35
# Программа: О, уже вечер!

time = input('Который сейчас час?(в формате чч:мм): ') # это ужасно но это работает

time = time[:2] + time[3:]

time = int(time)
if time > 2359 and time < 0:
    raise ValueError('Время указано не верно')

time = str(time)

time = time[:-2]
try:
    time = int(time)
except ValueError:
    print('Дата и время указаны не верно!')
    exit()

if time < 5:
    print('Сейчас ночь!')
elif time >= 5 and time <14:
    print('Cейчас утро!')
elif time >=14 and time <18:
    print('Сейчас день!')
elif time >=18 and time <=23:
    print('Сейчас вечер!')

# Задача №3
# Написать программу, которая спрашивает пользователя день его рождения (отдельно день и месяц цифрами) 
# и знает заранее текущее число (30 октября) Программа выводит количество дней до дня рождения. 
# datetime использовать нельзя. Циклы - можно.
# class date_of_birth:

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

current_day = 30

current_month = 10

current_day_of_year = sum(days_in_month[:current_month - 1]) + current_day

birth_day = input("Введите день рождения: ")
try:
    birth_day = int(birth_day)
except TypeError:
    print('День рождения укзан не верно!') 
    exit()  

birth_month = input("Введите месяц рождения: ")
try:
    birth_month = int(birth_month)
except TypeError:
    print('День месяца укзан не верно!') 
    exit()  


if birth_day <= 0 or birth_month <= 0:
    raise ValueError('месяц или день рождения указаны не верно!')

birth_day_of_year = sum(days_in_month[:birth_month - 1]) + birth_day


if birth_day_of_year > current_day_of_year:
    days_left = birth_day_of_year - current_day_of_year
elif birth_day_of_year < current_day_of_year:
    days_left = sum(days_in_month) - current_day_of_year + birth_day_of_year
elif birth_day_of_year == current_day_of_year:
    print('С днем рождения!')
    exit()    

print(f"До вашего дня рождения осталось {days_left} дней.")

































