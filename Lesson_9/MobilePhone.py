"""
Создать класс MobilePhone на основе класса Phone из пред ДЗ, у которого будут следующие атрибуты:
добавить свойства:
	is_busy - занято - когда кто-то позвонил до момента когда положили трубку должен иметь значение True
переопределить методы:
	- receive_call - теперь не только выводит фразу с именем но и сохраняет время и имя в историю. 
						Если в момент вызова трубка еще не положена - вернуть "занято".
добавить методы:
		- receive_sms - принимает имя и текст и сохраяет в историю
		- call_history - возвращает историю звонивших с датой и временем именем и случайным номером телефона формата +375*********		
		- sms_histiry - возвращает историю sms (имя/дата/время/текст)
		- сделать метод (положил трубку) 
		* метод receive_call принимает номер и если есть в справочнике в историю записать имя
		* положить трубку с возвратом  времени разговора которое тоже в записывается историю

"""

import time

class Phone:
    brand: str
    model: str
    issue_year: str
    call_history: list
    sms_history: list
    is_busy: bool = False
    hung_up: bool = True
    #call.start: time

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.call_history = []
        self.sms_history = []

    # def repr(self):
    #     return (f"Phone(Бренд: {self.brand}, Модель: {self.model}, Год выпуска: {self.issue_year}, История звонков: (str{call_history})")

    def __str__(self):
         return f" Бренд: {self.brand}\n Модель: {self.model}\n Год выпуска: {self.issue_year}\n История звонков: {self.call_history}\n История смс: {self.sms_history}"

    def receive_call(self, name, tel):
        if self.is_busy:
            print("Занято")
            return
        self.name = name
        self.call_history.append(["04.04.22", "10:01", name, tel])
        print(f"Звонит {self.name}")
        self.is_busy = True
        return " "

    def hung_up(self):
        if self.is_busy == True:
            print(f"Положить трубку")
        else:
            print(f"Перезвоните ещё раз")
        return None


    def view_call_history(self):
        res = " "
        for i in self.call_history:
            res += f"  дата: {i [0]}, время: {i [1]}, Имя: {i [2]}, tel: {i [3]}\n "
        return res

    def receive_sms(self, name_sms, text_sms):
        self.name_sms = name_sms
        self.text_sms = text_sms
        self.sms_history.append(["03.03.22", "12:11", name_sms, text_sms])
        #print(f"смс {self.name_sms}, текст {self.text_sms}")
        return " "

    def view_sms_history(self):
        res = "  "
        for i in self.sms_history:
            res += f" дата: {i[0]}, время: {i[1]}, Имя: {i[2]}, text: {i[3]}\n  "
        return res

    def get_info (self):
        return f"Бренд = {self.brand}, Модель = {self.model}, Год выпуска = {self.issue_year}"

p = Phone("Xiaomi Redmi", "10", 2022)
p.receive_call("Luda", "37529995999")
p.receive_sms("Luda", "Доброе утро")
time.sleep(1)
p.hung_up()
p.receive_call("Lena", "375296663322")
p.receive_sms("Lеna", "Добрый день")
time.sleep(2)
p.hung_up()
p.receive_call("Rita", "375294445511")
p.receive_sms("Rita ", "Добрый вечер")
time.sleep(2)
p.hung_up()
time.sleep(3)
p.get_info()
#p.repr()
print(p)
time.sleep(3)
print("_______________")
print(p.view_call_history())
print("_______________")
print(p.view_sms_history())
