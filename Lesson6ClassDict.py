#Сложности поиска нет, как в словаре, не   замедляет
"""a = dict()
a = dict(a=1, b=2, c='asd', d=None)
a = {1: 1}
Ключи всегда уникальные, упорядоченный тип (но нет индексов)
Ключом не может быть список , т.к это изменяемый тип, нехэшируемый
Множество тоже не может ыбть ключом словаря
a = dict([('a', 1), (1, 'q')])
dict - та же функция распаковки, как можно сделать через звездочку """
a = {'banana': 1, "apple": 234, "orange": 12}
print(a)
b = [1, 2, 4, 6]
print(b)
print(*b)#???

print(a["apple"]) #по ключу получаем значение
a = {'banana': {"q": 12, "c": 5}, "apple": 234, "orange": 12}
print(a['banana'])
print(a['banana']["q"])

c = a.get("banan", "banana") #значение получаем по ключу, 2ой аргумент показывает что если нет
print(c)
#доступ по квадратным скобкам норм, если данные из твоего файла. Если изменение, то прога упадет
#если данные из другого файла, то исполльзуем метод get
#if a.get('bas', False) is False: #проверили наш ключ на non-type , а потом проверили на False
"""for k, v in a.items():
    print(f'KEY: {key}', f'V: {value}')
    if key = 'apple' and value = 0:
        a[key] = 123 #т.е по словарю можно пробежатьься"""

#for v in a.values():
 #   print(v)

#a,setdefault('apple', 'asd') #если ключ существует , то значение возвращается
#еслм не существует, то создается со значением default (2ой аргумент)

a.clear()
a.pop()
b.fromkeys([1, 2, 3], "a") #из ключей делает значение, т.е. ключам из списка присвоили значения
print(b)

