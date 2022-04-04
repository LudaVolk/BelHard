"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""
def dict_from_args(*args, **kwargs):
    i = 1
    while True:
        if all([type(i) is int for i in args]) == False:
            print("Все позиционные аргументы должны быть целыми")
            break
        total = 0
        for arg in args:
            total += arg
        print('{')
        print('     "args_sum": ' + str(total) + ',')
        break
    num = 0
    if all([type(i) is int for i in kwargs]) == True:
        print("Все аргументы - ключевые слова должны быть строками")
        return
    for key, value in kwargs.items():
        if len(value) > num:
            num = len(value)
        #t = "{1}".format(key, value, end =" ")

    print('     "kwargs_max_len": ' + str(num))
    print('}')
args = [40000, 2, 8]

dict_from_args(*args, kw_1='Иван', kw_2='Иванова')
