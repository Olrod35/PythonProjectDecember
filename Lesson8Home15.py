#ДЗ 15. Декоратор
"""
Написать мини программу, которая будет проверять пароль пользователя и если пароль подходит будет авторизировать
пользователя:
Программа должна хранить Имена и Пароли в глобальном словаре
Должна содержать три функции:
check_password() возвращающая -> bool
authenticate() -> bool
login() принимающая минимум 2 аргумента username, password возвращающая -> bool
функция login() должна быть с декоратором в котором будет вся логика проверки check_password и authenticate
у пользователя должно быть 3 попытки после чего программа завершается и выводит сообщение "Попытки истекли!",
при каждой не удачной попытки должно быть сообщение "У вас осталось Н попыток"
Сценарий: пользователь с консоли вводит Имя и Пароль, программа возвращает текст "Вы в системе!" или "Не правильное Имя
или Пароль"
"""

from functools import wraps

USERS = {
    'Olha': '111111',
    'Talia': '222222'
}

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
    while i > 0:
        print("У Вас осталось", i, "попыток")
        username = input("Введите Ваш логин:")
        password = input("Введите Ваш пароль:")
        if login(username, password):
            break
        print("Неправильное имя или пароль")
        i -= 1
        if i == 0:
            print("Попытки истекли")

if __name__ == "__main__":
    main()
