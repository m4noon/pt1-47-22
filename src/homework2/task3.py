"""
3. Tuple practice
Создайте кортеж из одного элемента, чтобы при итерировании по
этому элементу последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""


tuple1 = ([1, 2, 3], )

for i in tuple1[0]:
    print(f'Значение из первого элемента кортежа: {tuple1[0][i-1]}')
