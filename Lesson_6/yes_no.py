"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
def yes_or_no(l: list):
    l2 = []
    for i in l:
        if l2.count(i) > 0:
            print("YES")
        else:
            l2.append(i)
            print("NO")

l = [1, 4, 3, 1, 5, 6, 7, 8, 7]
yes_or_no(l)



# def Lst(L):
#
#     #num = 0
#     elem = ' '
#     sorted(L)
#     for i in range(len(L)):
#         for j in range(len(L)):
#             L[i] = L[j]
#             if L[i-1] == L[i]:
#                 print('Yes')
#             else:
#                 print('No')
#          #   num = L[i]
#         else:
#             break
# my_list = [1, 8, 8, 3, 6, 8, 4]
#
# Lst(my_list)
#
#
#
#
#
