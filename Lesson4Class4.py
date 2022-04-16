a = 2
c = "text" if a > 1 else "text1"
print(c)

#for variable in iterator: - цикл прохода переменной по итерируемому объекту, т.е. каждый раз задаем
#переменной variable значение очередного элемента в последовательности iterator
for i in "text":
    print(i) #получаем 4 переменных с буквами
    #итерироваться можем по всем объектам, которые имеют скрытый метод iter

d=hasattr(123, "__iter__")#проверили наличие метода или атрибута iter
print(d)

e=hasattr("text", "__iter__")
print(e)

for i in "text":
    print(i)
else:
    print("Ok")# условия , которые выполняются при любом удачном завершении всех итераций.

for i in "text":
    if i == "e":
        break
    print(i)
else:
    print("Ok") #ok тоже будет напечатано, т.к break это не ошибка , а красивый выход из цикла

for i in "text":
    if i == "e":
        continue
    print(i)
else:
    print("Else")# циклл прервется и продолжится, просто не напечатает e
