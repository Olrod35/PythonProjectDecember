"""ДЗ16
В программу написанную в прошлом ДЗ добавить новый функционал (не изменяя старого)
username and password получать из командной строки как не обязательные аргументы.
Если оба аргумента переданы и имя и пароль прошли проверку то программа завершает работу не меняя прошлого поведения.
Если не правильное имя или пароль даем 3 попытки как и раньше.
Если передать только имя, то спрашивать только пароль, и наоборот.
Основная идея в том что-бы расширить функционал прошлой программы, а не переписывать!"""

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
        i -= 1
        print("У Вас осталось", i, "попыток")
        if i == 0:
            print("Попытки истекли")

if __name__ == "__main__":
    main()
