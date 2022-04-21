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
import random
from datetime import date, datetime, timedelta
current_data = date.today()
q = date.today() + timedelta(days=30)
import re
import strgen
import random

class User:
    name: str
    login: str
    password: str
    is_blocked: bool
    subscription_date: int
    subscription_mode: int

    def __init__(self, name, login, password, is_blocked=False, subscription_date=q, subscription_mode="free"):
        # self._name = name
        # self._login = login
        while self.check_name(name) is False:
            name = input("Введите имя: ")
            self.check_name(name)
            self.name = name
            break
        else:
            self.name = name

        while self.check_login(login, name) is False:
            login = input("Введите логин: ")
            self.check_login(login, name)
            self.login = login
            break
        else:
            self.login = login

        self.password = password
        self.is_blocked = is_blocked
        self.subscription_date = subscription_date
        self.subscription_mode = subscription_mode

    def get_info(self):
        print(f"name: {self.name}\nlogin: {self.login}\npassword: {self.password}\nsub_date: {self.subscription_date}\nsub_mode: {self.subscription_mode}")

    def block(self):
        self.is_blocked = True

    def unblock(self):
        self.is_blocked = False

    def check_subscr(self, date=None):
        current_data = date.today()
        if self.subscription_date <= date:
            print(f'{self.name} - перейдите на другой вид подписки')
        else:
            data = self.subscription_date - current_data
            print(f'{self.name} осталось {data.days} дней подписки, вид подписки {self.subscription_mode}')

    def check_name(self, name):
        if len(re.findall("[а-яА-ЯёЁ]", name)) == len(name):
            return True
        else:
            print(f'{name} - Введите новое имя')
            return False

    def check_login(self, login, name):
        if re.match(r"([A-Za-z0-9+_]{6,})", login):
            return True
        else:
            print(f'{name} - Введите новый логин')
            return False

    def check_password(self):
        val = self.password
        if re.match(r"([A-Z][a-z][0-9]{1,6})", val):
            print(f'{self.name} - пароль соответствует')
        else:
            print(f'{self.name} - пароль не соответствует')
            return False

    def change_pass(self, val):
        if val == "":
            new_password = ""
            for x in range(15):
                new_password = strgen.StringGenerator("[A-Z][a-z][0-9]{6}").render()
            val = new_password
        else:
             if self.check_password(val):
                print(new_password)

        if re.search(r"([A-Z][a-z][0-9]{1,6})", val):
            print(f'{self.name} - new_password', val)
            self.password = val
        else:
            print(f'{self.name} - поменяйте пароль')

user1 = User("Люда", "Qq_123", "Ll2345")
user2 = User("Лена", "Ww_234", "Aa2345")
user3 = User("ира", "Gg_123", "")
user1.get_info()
user1.block()
user1.unblock()
# user1.change_pass('')
#user1.check_subscr('')
#user1.change_pass()
print("-----------")
user2.get_info()
user2.block()
user2.unblock()
# user2.change_pass('')
print("-----------")
user3.get_info()
user3.block()
user3.unblock()
user3.change_pass('')
