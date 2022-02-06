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

def main():
    args = stroka_parser()
    username = args.user
    password = args.password
    print(username)
    i = 3
    while i > 0:
        username = username or input("Введите Ваш логин:")
        password = password or input("Введите Ваш пароль:")
        if login(username, password):
            break
        print("Неправильное имя или пароль")
        i -= 1
        print("У Вас осталось", i, "попыток")
        if i == 0:
            print("Попытки истекли")

if __name__ == "__main__":
    main()