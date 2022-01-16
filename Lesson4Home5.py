d = '*'
n = int(input('Введите высоту треугольника: '))
p = n * " "
m = n
for i in range(n):
    a = print(p[0:m] + d * (i + 1) + d * i)
    m -= 1
