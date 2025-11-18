# Компьютер запрашивает у пользователя число N
# и создает таблицу (списки вложенные в список)
# размером N строк на N столбцов, заполненную
# следующим образом:
N = int(input("Введите число N: "))

table = (
    [] if N <= 0 else
    [[1 if j == i else 0 for j in range(N)] for i in range(N)]
)

for row in table:
    print(row)
    
