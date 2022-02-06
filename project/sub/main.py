# import datetime, functools, collections
import requests #все импорты перед фром.
from requests import get, post, put
from requests.exeptions import HTTPError
from requests import exceptions
from collections import defaultdict as df \ #берем из коллекции и меняем имя
    Counter, \
    OrderedDict as OD #а можно переносить при помощи tuple
from collections import (
    defaultdict as df,
Counter,
OrderedDict as OD

#Import Built-in, потом сторонние, потом встроенные. Все импорты в нач файла
def fanc():
    ...
import datetime #noqa

def main():
    df(a=1)

if __name__ =='__main__':
    main()

CONST = 1 #тут норм переменная

def main():
    print(CONST)

from sub.new import * #noqa #если хотим определить переменные в конце кода
#тут переопределили перемен из переменного окружения

Импорт есть абсолютный, а есть необсолютный
from sub import new #(это относительный импорт, если на этом же уровне вложенности)
from project.main import main #это абсолютный импорт (если находимся глубже)

