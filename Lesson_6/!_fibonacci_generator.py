"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = 5
fib = fibonacci(n)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# def fibonacci(n):
#     if (n <= 1):
#         return n+1
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))
# while True:
#
#     n = input("Введите число членов последовательности:")
#     if not n.isnumeric():
#         print('Введите  число')
#     elif int(n) <= 0:
#         print('Введите число больше 0')
#     else:
#         break
# print("Последовательность Фибоначчи:")
#
# for i in range(int(n)):
#     print(fibonacci(i))