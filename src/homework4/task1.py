"""
Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов,
не только текущий запуск программы)
"""


import os


def dec(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if not os.path.exists('task1.txt'):
            with open('task1.txt', 'w'):
                pass

        with open('task1.txt', 'a') as log:
            log.write(f'Результат вызова функции: {result}\n')

        return result

    return wrapper


def summary(a, b):
    return a + b


print(dec(summary)(5, 10))