"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
def Lst(L):

    num = 0
    for i in range(len(L)):
            if L[i] == num:
                print('Yes')
            else:
                print('No')
            num = L[i]
my_list = [1, 5, 6, 6, 8, 8]

Lst(my_list)
