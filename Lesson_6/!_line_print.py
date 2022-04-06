"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на 4 пробела

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""
#исправлено
def line_print(l, d=0):
    for item in l:
        if type(item) is list:
            line_print(item, d+1)
        else:
            print("     " * d + str(item))

some_list = [1, 2, [1, 2, [5, 7], 3], 8]
line_print(some_list)






# def line_print(some_list):
#     for i in iter(some_list):
#         if type(i) == list:
#            for j in iter(i):
#                if type(j) == list:
#                    for k in iter(j):
#                        print('         ' + str(k))
#                else:
#                   print('    ' + str(j))
#         else:
#             print(str(i))
#
# some_list = [1, 2, [1, 2, [5, 7], 3], 8]
# result = line_print(some_list)
#
#
# def rec(spicok, level=1):
#     print(*spicok, 'level=', level)
#     for i in spicok:
#         if type(i) == list:
#             rec(i, level + 1)
#
# a = [1, 2, [1, 2, [5, 7], 3], 8]
# rec(a)



