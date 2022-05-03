"""
Слова как химические элементы
Каждый химический элемент из таблицы Менделеева характеризуется своим обозначением,
состоящим из одного, двух или трех символов. Есть такая игра – пытаться выразить то или
иное слово через химические элементы. Например, слово silicon может быть записано при помощи
следующих химических элементов: Si, Li, C, O и N. В то же время слово hydrogen не может быть
составлено из названий элементов.
Напишите рекурсивную функцию, способную определять, можно ли выразить переданное ей слово
исключительно через обозначения химических элементов. Ваша функция должна принимать два параметра:
слово, которое нужно проверить, и список символов, которые можно при этом использовать.
Возвращать функция должна строку, состоящую из использованных символов, если собрать искомое
слово можно, и пустую строку в противном случае. При этом регистры символов учитываться не должны.
В основной программе должна быть использована ваша функция для проверки всех элементов таблицы
Менделеева на возможность составить их названия из обозначений химических элементов.
Отобразите на экране названия элементов вместе с обозначениями, которые были использованы
для их написания. Например, одна из строчек может выглядеть так:
Silver может быть представлен как SiLvEr
Для решения задачи используйте набором данных с химическими элементами,
который находится в файле elements.txt.
"""


def check_word(word: str, list_of_elements: list) -> str:
    """Проверяет можно ли выразить введённое слово через таблицу Менделеева

    :param word: Введённое слово
    :param list_of_elements: Список всех элементов из таблицы Менделеева
    :return: Возвращает слово, если его можно выразить через таблицу. Если нельзя - None
    """
    for i in (3, 2, 1):
        start_word = word[:i]
        if start_word not in list_of_elements:
            continue
        if len(word) == i:
            return start_word
        end_word = check_word(word[i:], list_of_elements)
        if end_word:
            return start_word + end_word


def main():
    word = input('Введите слово на английском: ').lower()

    with open('elements.txt', 'rt') as file:
        elements = file.read().lower().split(",")

    list_of_elements = elements[1::2]
    new_word = check_word(word, list_of_elements)

    if new_word is None:
        print('Введённое слово невозможно выразить через таблицу элементов Менделеева')
    else:
        print(f'Слово {new_word} можно выразить через таблицу элементов Менделеева')


if __name__ in '__main__':
    main()