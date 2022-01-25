#ДЗ12
"""Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).
Пример:
checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1"""

def checkio(k):
    stroka = str(k)
    spisok = []
    for i in stroka:
        spisok.append(int(i))
    proizv = 1
    for i in spisok:
        if i != 0:
            proizv *= i
    return proizv

k = input("Введите целое число: ")
print(checkio(k))