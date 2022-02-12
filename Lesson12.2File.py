# f = open("TExtWork.txt", "r")
# print(f, seek(0,7)) - нулевая строка и 7ой столбец
# f.close() #обязательно закрывать

# r - read
# w - write
# a - append
# b - byte
# t - textwrap
# + - read and write
# x - выкид исключения

# try:
#     f = open("TExtWork.txt", "w")
# #data = f.readlines()
#     f.writelines("ffff")
#     f.write("\nnew text")
# finally:
#     f.close()

# try:
#     f = open("TExtWork.txt", "r")
#     data = f.read()
#     print(data)
#     print("*"*50)
#     f.seek(0,0)#метод вернул курсор в нулевую позицию
#     print(f.read())
# finally:
#     f.close()

"""def main():
    with open("TExtWork.txt", "r") as f: #Менеджер контекста - это класс, в котором есть 2 метода
    #а метод - это функция, принадлежащая классу
   # Это 2 метода:
    #__enter__
    #__exit__
    #Наличие этих методовд говорит о том, что наш класс можно использовать через мен конт
   # data = f.read() можно задать перемен здесь, а можно отдельно
        return f.read()

if __name__ == "__main__":
    data = main()
    print(data)"""

"""def main(data):
    with open("TExtWork.txt", "w") as f: #Менеджер контекста - это класс, в котором есть 2 метода
        for st in data:
            f.write(f"{st}\n")

if __name__ == "__main__":
    data = [
        "gggg"
        "gggg"
    ]
    main(data)
    #print(data)"""

def main(data):
    f = open("TExtWork.txt", "r+")
    f.write("aaaa")
    print(f.read())
    with open("TExtWork.txt", "w") as d:
        for st in data:
            d.write(f"{st}\n")

if __name__ == "__main__":
    data = [
        "kkkkk"
        "mmmmm"
    ]
    main(data)
    