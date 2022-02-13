#ДЗ18
# Написать собственный клас Исключения - UserDoesNotExist
#Переписать функцию проверки пароля, используя собственное исключения

from functools import wraps
class UserDoesNotExist(Exception):
    ...


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
    try:
        if USERS.get(username) == password:
            return True
        elif username not in USERS:
            raise UserDoesNotExist
    except UserDoesNotExist:
        print("Пользователя не существует")

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
        print("Неправильный пароль")
        i -= 1
        if i == 0:
            print("Попытки истекли")

if __name__ == "__main__":
    main()