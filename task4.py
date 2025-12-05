"""
Задача 4. Количество маршрутов короля
На доске 8×8 король стоит в верхнем левом углу и может двигаться вправо, вниз или по диагонали (вправо-вниз).
Найти количество маршрутов в правый нижний угол.
Ответ: одно число.

ПРОГРАММА ДОЛЖНА ПЕЧАТАТЬ НА ЭКРАНЕ ТОЛЬКО ОДНО ЧИСЛО (ОТВЕТ) И НИЧЕГО БОЛЬШЕ.
"""

# Решение будет здесь


import numpy as np

sum = 0
rang = 8
start = 0
end = 30

a = [[0 for _ in range(rang)] for _ in range (rang) ]

a[0][0] = 1

for x in range (rang):
    for y in range(rang):
        moment_ways = a[x][y]
        moment_value = start + x + y
        #if moment_value == 30:
        #    sum += moment_ways
        if x + 1 < rang:
            a[x+1][y] += moment_ways
        if y + 1 < rang:
            a[x][y+1] += moment_ways
        if (y + 1 < rang) and (x + 1 < rang):
            a[x+1][y+1] += moment_ways
        #if z + 1 < rang:
        #    a[x][y][z+1] += moment_ways

print(a[7][7])
