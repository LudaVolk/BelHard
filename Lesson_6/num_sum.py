"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(L):
    if len(L) == 1:
        return 0
    else:
        return L[0] + sum(L[1:])

i = [6, 4, 13]

print(sum(i))