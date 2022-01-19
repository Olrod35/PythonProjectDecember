"""Даны два списка чисел (можно сгенерировать при помощи
генератора случайных чисел). Посчитайте, сколько
уникальных чисел содержится одновременно как в первом списке,
так и во втором.
Множество использовать нельзя"""

m = [6, 8, 10, 78, 68]
n = [8, 9, 23, 78, 64]

for i in m:
    for p in n:
        if i == p:
            m.remove(i)
            n.remove(p)
t = m + n
print(t)
print(len(t))


"""
import random

a = [random.randint(15, 150) for _ in range(10)]
b = [random.randint(15, 150) for _ in range(10)]
print(len([i for i in [*a, *b] if [*a, *b].count(i) == 1]))"""

