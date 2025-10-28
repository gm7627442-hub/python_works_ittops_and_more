speed_1 = input('уажите скорость первой машины: ')
speed_1 = int(speed_1)


speed_2 = input('уажите скорость воторй машины: ')
speed_2 = int(speed_2)

if speed_1 and speed_2 <= 0:
    raise ValueError('Обе машины не двигаються!')


distance = input('Укажите растояние между машинами: ')
distance = int(distance)
if distance == 0 :
        raise ValueError('Мышины уже рядом')

direction = input('Машины двигаються к дргу другу| 1 - да | 2 - нет |: ')
direction = int(direction)
if direction == 2: 
        raise ValueError('Мышины никогда не окажуться рядом')
elif direction != 1:
        raise ValueError('Вы указали не верные данные')

result_1 = speed_1 + speed_2

result_2 = distance / result_1

print('Дано: ', '\n', 'Скорость перовй машины: %i км/ч' % speed_1, '\n', 'Скорость второй машины: %i км/ч' % speed_2, '\n', 'Расстояние между машинами: %i км' % distance)
print('Найти: ', '\n', 'Через какое время машины окажуться рядом')
print('Решение: ', '\n', 'Скорость первой машины сложить со второй: %iкм/ч' % result_1, '\n', 'поделить полученный результат на растояние: %i' % result_2)
print('Ответ: %0.2f часа(-ов)' % result_2 )

