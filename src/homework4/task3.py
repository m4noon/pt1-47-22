"""
Двоичная пирамида.
На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
a. Перевести числа от m до n (включительно) в двоичные числа.
b. Сложить полученные двоичные числа по основанию 10.
c. Перевести результат сложения в двоичную число.
d. Вернуть строку с результатом.
"""


def converter(m: int, n: int) -> str:
    """Функция выполняет действия, поставленные в условии задачи

    :param m: Введённое число
    :param n: Введённое число
    :return: Результат преобразования
    """
    numbers_2 = []
    for i in range(m, n + 1):
        numbers_2.append(int(format(i, 'b')))
    sum_number_2 = sum(int(x) for x in numbers_2)
    result = format(sum_number_2, "b")

    return result


def main():
    m, n = -1, -1
    while not(0 <= m <= n):
        print('Введите числа m и n так, чтобы вополнялось условие: 0 <= m <= n')
        m = int(input('Введите число m: '))
        n = int(input('Введите число n: '))

    print(f'Результат выполнения функции: {converter(m, n)}')


if __name__ == '__main__':
    main()