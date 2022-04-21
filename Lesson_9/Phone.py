"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


# class Phone:

    # def __init__(self, brand, model, issue_year):
#         self.brand = brand
#         self.model = model
#         self.issue_year = issue_year
#
#     def receive_Call(self, name):
#         print("Звонит", name)
#
#     def __str__(self):
#         self.get_info()
#
#     def get_info(self):
#         #return f"Брэнд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"
#         print(f"Брэнд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}")
#
# #p = Phone(input('Бренд: '),
#           #input('Модель: '),
#           #input('Год выпуска: '))
#
# p1 = Phone('Xiaomi Redmi', 10, 2022)
# p2 = Phone('Xiaomi Redmi', 9, 2021)
# p3 = Phone('Xiaomi Redmi', 8, 2020)
# p4 = Phone('Xiaomi Redmi', 7, 2019)
# #print(p.get_info())
# p1.get_info()
# p1.receive_Call("Люда")
# print("________________")
# p2.get_info()
# p2.receive_Call("Лера")
# print("________________")
# p3.get_info()
# p3.receive_Call("Таня")
# print("________________")
# p4.get_info()
# p4.receive_Call("Даша")
# print("________________")

class Phone:
    brand: str
    model: str
    issue_year: int

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def __repr__(self):
        return f"Phone({self.brand}, {self.model}, {self.issue_year})"

    def receive_call(self, name):
        self.name = name
        print(f"Звонит: {self.name}")
        return "   "

    def get_info(self):
        return f"Брэнд:{self.brand}\nМодель:{self.model}\nГод выпуска:{self.issue_year}"

p1 = Phone("Xiaomi Redmi", "10", 2022)
p2 = Phone("Xiaomi Redmi", "9", 2021)
p3 = Phone("Xiaomi Redmi", "8", 2020)
p4 = Phone("Xiaomi Redmi", "7", 2019)
pl = [p1, p2, p3, p4]

print(repr(pl))
print("________________")
print(str(p1))
print("________________")
print(p1.get_info())
p1.receive_call("Люда")
print("________________")
print(p2.get_info())
p2.receive_call("Даша")
print("________________")