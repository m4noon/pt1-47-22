"""
Переводим меры
Во многих кулинарных книгах до сих пор можно встретить рецепты, в которых ингредиенты отмеряются
стаканами, чайными и столовыми ложками. И хотя при наличии этих нехитрых предметов таким рецептам
следовать довольно удобно, бывает трудно быстро преобразовать подобные меры при приготовлении
рождественского ужина на огромную семью. Например, если в рецепте сказано взять четыре столовые
ложки того или иного ингредиента, то при увеличении выхода в четыре раза можно просто отсчитать
16 столовых ложек. Однако гораздо проще было бы привести эту меру к одному стакану.
Напишите функцию, выражающую заданный объем ингредиентов с использованием минимально
возможных замеров. Функция должна принимать в качестве параметра количество единиц измерения,
а также их тип (стакан, столовая или чайная ложка). На выходе мы должны получить строку,
представляющую указанное количество вещества, с задействованием минимального количества
действий и предметов. Например, если на вход функции вы подали объем, равный 59 чайным ложкам,
возвращенная строка должна быть такой: «1 cup, 3 tablespoons, 2 teaspoons».
Подсказка. Один стакан вмещает 16 столовых ложек,
а одна столовая ложка эквивалентна трем чайным ложкам.
"""


def converse(component: dict) -> dict:
    """Конвертирует ингридиенты по правилу из условия задачи

    :param component: Словарь введённых компонентов
    :return: Конвертированный словарь
    """
    while component.get('teaspoon') >= 16:
        component['cup'] += 1
        component['teaspoon'] -= 16

    while component.get('teaspoon') >= 3:
        component['tablespoon'] += 1
        component['teaspoon'] -= 3

    if (component.get('tablespoon') * 3) // 16 >= 1:
        while component.get('tablespoon') >= 6:
            component['cup'] += 1
            component['teaspoon'] += 2
            component['tablespoon'] -= 6
        converse(component)

    return component


def main():
    component = {
        'cup': 0,
        'tablespoon': 0,
        'teaspoon': 0
    }

    for key in component:
        value = int(input(f'Введите количество {key}: '))
        component[key] = value

    print(f'Количество ингредиентов с минимальным использованием замеров: {converse(component)}')


if __name__ in '__main__':
    main()
