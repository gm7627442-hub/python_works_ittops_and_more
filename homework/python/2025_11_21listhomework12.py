import random

n = random.randint(0, 10)

lst = [random.randint(-100, 100) for _ in range(n)]
print("Список:", lst)

if not lst:
    predmax = None
else:
    m = max(lst)  

    without_max = [x for x in lst if x != m]

    if not without_max:
        predmax = None
    else:
        predmax = max(without_max)

print("Предмаксимум:", predmax)
