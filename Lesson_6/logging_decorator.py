"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""
#работа над ошибками
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем функцию {func.__name__} c аргс {args} и c кваргс {kwargs}")
        func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
    return wrapper

@decorator
def hello(name, surname, v1=True, v2=2):
    print(f"Привет {surname} {name} {'!' if v1 else ''}")

name = "Люда"
surname = "Волкова"

hello(name, surname, v1=False, v2=3)
