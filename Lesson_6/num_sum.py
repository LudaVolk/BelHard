"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""
#1я попытка
def sum_of_numbers(n: int, s = 0):
	n = str(n)
	if s == len(n): return 0
	return sum_of_numbers(n, s+1) + int(n[s])
n = 1235
print(sum_of_numbers(n))

#2я попытка
def sum_of_numbers(L):
    if len(L) == 1:
        return 0
    else:
        return L[0] + sum(L[1:])

i = [1, 2, 7]

print(sum(i))



