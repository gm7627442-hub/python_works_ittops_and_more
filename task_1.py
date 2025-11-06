# Задача №1
# Написать программу, которая спрашивает у пользователя целое количество часов и выводит количество часов до сна (23:00) Пример работы:
# Программа: Который час?
# Пользователь: 19
# Программа: до сна часов: 4 
 
# Разделить код на три файла Павел К. 
# Код не работает ошибка типов  Павел К.
# отсттвуют коментарии(сам не одного не написал!) Павел К.


time_now = input("Который час: ") # было бы не плохо утачнить для пользовтаеля формат вводимго времени Павел К.
try:
    time_now = int(time_now)
except ValueError:
    print("вы ввели не число")
    time_now = None # более красиво и читаемо было бы написать прото exit() Павел К.
    time_count = None
    
if time_now: # не очень зачем нужен этот if Павел К.
    time_sleep = 23
    time_count = time_sleep - time_now 
    print(type(time_count))  # Лишняя строчка, зачем выводить пользователю тип переменной? Павел К.
if time_count == 1:
    print("До сна: ",time_count, "час")  # довольно элегантное решение, но не все варианты будут коректны например: до сна осталось 2 часов Павел К.
                                                          
else:                         
    print("До сна часов: ", time_count) 



# Задача №2
# Написать программу, которая спрашивает у пользователя, который час и выводит в ответ время суток. 
# Границы определить любые, но в каждом времени суток должно быть непустое количество часов. 
# Пример работы программы:
# Программа: Который час?
# Пользователь: 19:35
# Программа: О, уже вечер!

time_now = input("Который час: (минуты и часы через \":\") ") # плохая читаемость я  добавил пропуск между строчками  Павел К.
time_now = time_now.split(":") # комент выше относиться ко всему коду ниже кроме тех мест где прпуск ставить не нужно например после if Павел К.
# try:
#     if time_now[0] > 23 or time_now[1] > 59:
#         raise VallueError("Таких времени не существует")  # убрал бы лишнее из кода это сильно повышает читаемость Павел К.
# except ValueError as e:
#     print("вы ввели не число")   
time_now = time_now[0] 
print(time_now) 
if time_now[1] >= 0 and time_now[1] <= 30: 
   time_now[0] += 1  
print(time_now)   
try:
    time_now = int(time_now)
except ValueError:
    print("вы ввели не число")
    time_now = None
if time_now:
    if time_now > 4 and time_now <= 9:
        print("Сейчас утро")
    elif time_now > 9 and time_now <= 16:
        print("Сейчас день")
    elif time_now > 16 and time_now <= 22:
        print("Сейчас вечер")
    elif time_now > 22 and time_now <= 24:
        print("Сейчас ночь")
    elif time_now >= 0 and time_now <= 4:
        print("Сейчас ночь")
    

   
# Задача №3
# Написать программу, которая спрашивает пользователя день его рождения (отдельно день и месяц цифрами) и
# знает заранее текущее число (30 октября) 
# Программа выводит количество дней до дня рождения. datetime использовать нельзя. Циклы - можно
dict_mes = {1 : 31, 2 : 28, 3 : 31, 4: 30, 5 : 31,\
    6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
birsday = input("Введите свой день рождения (отдельно день и месяц цифрами): ")
birsday = birsday.split(".")
print(birsday)
day_now = 30
mes_now = 10
birsday_day = int(birsday[0])
birsday_mes = int(birsday[1])

day_count = day_now - birsday_day
# mes_count = mes_now - birsday_mes

print(day_count)
# print(mes_count)
mes_day = 0
for i in range(1, birsday_mes):
    mes_day += dict_mes[birsday_mes]
day_all = day_count + mes_day    
print(mes_day)
print("Дней до дня рождения: ", day_all) 
   
print(dict_mes[birsday_mes])




