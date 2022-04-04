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

def line_print(some_list):
    for i in iter(some_list):
        if type(i) == list:
           for j in iter(i):
               if type(j) == list:
                   for k in iter(j):
                       print('         ' + str(k))
               else:
                  print('    ' + str(j))
        else:
            print(str(i))

some_list = [1, 2, [1, 2, [5, 7], 3], 8]
result = line_print(some_list)



