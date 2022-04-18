"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цыфры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
					содержит менее шести символов
					содержит строчную букву
					содержит заглавную букву
					содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
"""
import re
import strgen
from datetime import date


class User():

    def __init__(self, name, login, password, is_blocked):
        self._name = name
        self._login = login
        self._password = password
        self.is_blocked = False
        self.subscription_date = date.today()
        self.subscription_mode = "free"


    @property
    def name(self):
         return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def bloc(self, is_blocked):
        self.is_blocked = is_blocked
        if is_blocked != True and is_blocked != False:
            self.is_blocked = False
        else:
            self.is_blocked = is_blocked

        if self.is_blocked:
           print("Пользователь заблокирован")
        else:
           print("Пользователь не заблокирован")

    def get_info(self):
        print(f"name = {self._name}, login = {self._login}, password = {self._password}")

    def check_subscr(self):
        date1 = date.today()
        date2 = date(2022, 1, 11)
        namber_date = (date1 - date2).days
        if namber_date >= 30:
            return "paid"
        else:
            return "free"

def change_pass(new_password):
    if len(new_password) >= 0:
        password = strgen.StringGenerator("[A-Z][a-z][0-9]{4}").render()
        print("новый пароль:" + password)
    else:
        print("новый пароль:" + new_password)
        # return new_password
    return password

while True:
    name = input("Введите имя: ")
    if re.match(r"[а-яА-ЯёЁ]", name):
        break
    else:
        print('Имя не корректно')
        continue
while True:
    login = input("Введите логин: ")
    if re.match(r"([A-Za-z0-9+_]{6})", login):
        break
    else:
        print('Логин не валиден')
        continue

while True:
    password = input("Введите пароль: ")
    if len(password) == 0:
        password = change_pass(password)
        break
    elif re.match(r"([A-Z][a-z][0-9]{1,6})", password):
        break
    else:
        print('Пароль не валиден')
        continue

# while True:
#     date_i = str(input('Ведите дату в формате Y,m,d: '))
#     try:
#         date2 = date.strptime(date_i, "%Y,%m,%d")
#         #date2 = check_subscr(date2)
#         break
#     except ValueError:
#         print("Введите дату правильно")
#         continue

user = User(name, login, password, True)
user.name = name
user.login = login
user.password = password
#print("имя:" + user.name, "логин:" + user.login, "пароль:" + user.password)
user.get_info()
user.bloc(False)
print("Subscription_mode: " + user.check_subscr())

