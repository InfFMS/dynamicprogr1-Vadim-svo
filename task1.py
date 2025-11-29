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
rang = 15


a = [[[0 for _ in range(rang)] for _ in range (rang) ] for _ in range (rang)]

a[0][0][0] = 20

for x in range (rang):
    for y in range(rang):
        for z in range(rang):
            if a[x][y][z] == 30:
                sum += 1
                continue

            if a[x][y][z] > 0 and a[x][y][z] < 30:
                if x+1 < rang:
                    a[x+1][y][z] = a[x][y][z] + 1
                if y+1 < rang:
                    a[x][y+1][z] = a[x][y][z] + 2
                if z+1 < rang:
                    a[x][y][z+1] = a[x][y][z] + 4


print(sum)