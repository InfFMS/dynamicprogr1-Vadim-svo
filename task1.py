"""
Задача 1. Исполнитель «Плюс»
Исполнитель может выполнять команды: +1, +2 и +4.
Начальное число: 20. Конечное число: 30.
Требуется определить количество различных программ, приводящих число 20 к числу 30.
Ответ: одно число.

ПРОГРАММА ДОЛЖНА ПЕЧАТАТЬ НА ЭКРАНЕ ТОЛЬКО ОДНО ЧИСЛО (ОТВЕТ) И НИЧЕГО БОЛЬШЕ.
"""

# Решение будет здесь

import numpy as np

sum = 0
rang = 100
start = 20
end = 30

a = [[[0 for _ in range(rang)] for _ in range (rang) ] for _ in range (rang)]

a[0][0][0] = 1

for x in range (rang):
    for y in range(rang):
        for z in range(rang):
            moment_ways = a[x][y][z]
            moment_value = start + x*1 + y*2 + z*4

            if moment_value == 30:
                sum += moment_ways

            if x + 1 < rang:
                a[x+1][y][z] += moment_ways
            if y + 1 < rang:
                a[x][y+1][z] += moment_ways
            if z + 1 < rang:
                a[x][y][z+1] += moment_ways

print(sum)
