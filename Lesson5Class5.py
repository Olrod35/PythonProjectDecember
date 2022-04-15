a = [15, 23, 56]
for i in range(10):
    a.append(i)
print(a)

b = [i for i in range(10)]
print(b)

c = [i for i in range(10) if i > 5] #проверка
print("c=", c)

d = [i == 3 for i in range(10)]
print("d=", d)

e = [i for i in range(10) for j in range(i)] #цикл в цикле
print(e)

import random
f = [random.randint(10, 20) for _ in range(5)] #5 чисел от 10 до 20
print(f)

k = random.choice(f)# элемент из списка f
print(k)

g = random.choice([i for i in range(10)]) #выбирается элемент из списка
print(g)


del c
print("c=", c) #список и переменная уже исчезли

CARS_BRAND = ('kia', 'bmw', 'vw')
print(CARS_BRAND)
kia = CARS_BRAND[0]
print(kia)
kia, toyota, bmw = CARS_BRAND #распаковка
print(toyota)

l = tuple(b)
print(l)