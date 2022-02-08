#Дз17
"""Расширить функционал прошлого ДЗ:
Имитировать неудачную попытку входа в систему с блокировкой пользователя на 5 минут.
Выводить сообщение "Вы заблокированы! Следующая попытка через N мин."
для решение понадобится
хранить дату/время - последняя НЕ удачная попытка входа
действия с датой лучше вынести в отдельные функци
т.к. мы не храним данные пользователя в базе данных или файле мы имитируем такую ситуацию,
в нашем случае программа всегда будет выводить сообщение "Вы заблокированы!
Следующая попытка через N мин."""

from functools import wraps

USERS = {
    'Olha': '111111',
    'Talia': '222222'
}

import argparse
import datetime

print(datetime.datetime.now())

def stroka_parser():
    parser = argparse.ArgumentParser(add_help=False)#Создали экземпляр
    parser.add_argument("--user", action="store")#Передача User в качестве ком строки
    parser.add_argument("--password", action="store")
    return parser.parse_args()

def decorator_for_login(func):
    def wrapper(username, password):
        if not check_password(username, password):
            return False
        if not auth():
            return False
        return func(username, password)
    return wrapper

def auth():
    return True

def check_password(username, password):
    if USERS.get(username) == password:
        return True
    #return USERS.get(username) == password

@decorator_for_login
def login(username, password):
    print("Вы в системе!")
    return True

def func_time():
    date_fix = datetime.datetime.now()
    print(date_fix)
    date_fix_str = date_fix.strftime("%m/%d/%Y/%H/%M/%S")
    print(date_fix_str)
    date_fix_obj = datetime.strptime(date_fix_str, "%d/%m/%Y %H:%M:%S")
    print(date_fix_obj)
    if datetime.datetime.now() < date_fix_obj + datetime.timedelta(minutes=1):
         print("время")

def main():
    i = 3
    print("У Вас", i, "попыток")
    while i > 0:
        args = stroka_parser()
        username = args.user
        password = args.password
        if username is not None:
            print(username)  # напечатать то, что из командной строки
        username = username or input("Введите Ваш логин:")
        password = password or input("Введите Ваш пароль:")
        if login(username, password):
            break
        print("Неправильное имя или пароль")
        print("Вы заблокированы! Следующая попытка через 1 мин.")
        func_time()
        i -= 1
        print("У Вас осталось", i, "попыток")
        if i == 0:
            print("Попытки истекли")

if __name__ == "__main__":
    main()