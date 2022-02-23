"""
Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа
от 1 до 20, а значениями кубы этих чисел.
"""


dictionary = {a: a**3 for a in range(1, 21)}
print(f'Словарь, значения которого являются кубы ключей:\n{dictionary}')