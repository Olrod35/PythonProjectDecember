#Дан список чисел. Определите, сколько в этом списке
# элементов, которые больше двух своих соседей (слева и справа),
#и выведите количество таких элементов.
#Крайние элементы списка никогда не учитываются,
# поскольку у них недостаточно соседей.
k = 0
list1 = [456, 752, 25, 38, 4, 8]

i = 0
for (index, elem) in enumerate(list1):
    if index == 0:
        print(elem)
    if index == len(list1) - 1:
        print(elem)

    if list1[i] < list1[i+1] and list1[i] > list1[i-1]:
        print("yes")
    i += 1



      #  k += 1
#print(k)
