# import os # получение переменных окружения
#
# #print(os.listdir('.'))
#
# def main(start_path):
#     result_dict = {}
#     for root,dirs, files in os.walk(start_path):
#         for i, filename in enumerate(files):
#         fullpath = os.path.join(root, filename)
#         result_dict.update({i: fullpath})
#     return result_dict
#
# if __name__ == "__main__":
#     res = main(".")
#     pp(res)

#Eval() Берет строку и ввыполняетт содержимое как пайтон код

"""def func(_x):
    return _x*_x
    func(x)"""

if __name__=="__main__":
    x = 2
    y = 6
    res = eval("sum([x+y, x*y, 56-23])", {"x": 4, "y": 6}) #locals , globals словари - аргумегты
    print(res)
    res1 = eval("print([i for i in range(10)])") #нельзя if

    print(res1)
#лучше не использовать, т.к данная функция неявная
    ff = "def func(_x): return _x*_x\nprint(f(x))" #exec принимает весь синтаксис Python
    res_2 = exec(ff,{"x": 2}) #типа eval
print(res_2)


