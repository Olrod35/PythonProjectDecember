"""try:
    ...
except Exception:
    ...
else:
    ...
finally:
    ..."""

"""a = {1: 2}
try:
    value = a[6]
except Exception: #базовое исключение, но его использование - правило плохого тона
    breakpoint() #позволит глянуть, есть ли исключение
    value = a[1]
    print("Ok")

print(value)"""

"""BaseException:
    SystemExit
    KeyBoardInterrupt
    GeneratorExit
    Exception:
        StopIteration
        ArithmeticError:
            FloatingPointError
            ZeroDivisionError

        AssertionError
        AttributeError
        EOFError
        ImportError
        LockupError"""
"""a = {1: 3}
try:
    value = a[6]
    b = 4 / 0
except(KeyError, ZeroDivisionError):
    value = a[1]
    print("ok")
except ZeroDivisionError as err:
    print("ZeroDivEr", err)
else: #отработает, если все хорошо и исключение не вызвалось
    print("good")
    try:
        ...
    except Exception:
        ...
    print("else")

b = "fgli123rr"
try:
    b = int(b)
except ValueError as err:
    print("ValueError", err)
else:
    print("good")
finally: #конструкция отработает в любом случае
    print("finally")
"""
"""class MyException(Exception):
 ...

def main(x, y):
    d = {1: 2, 4: 6}
    assert y != 0
    try:
        return d[x] / y
    except (KeyError, ZeroDivisionError):
        raise MyException #для того, чтобы функцию обернуть еще в одно искл и отловить наше созданное

if __name__ == "__main__":
    try:
        main(4, 0)
    except (MyException, ValueError, AssertionError):
        print("Error")"""
class Small(Exception):
    ...

class Large(Exception):
    ...
d = 10

def main():
    while True:
        try:
            i = int(input("Enter digit: "))
            if i > d:
                raise Large
            elif i < d:
                raise Small
        except Small:
            print("Small")
        except Large:
            print("Large")
        else:
            break

if __name__ == "__main__":
    main()
