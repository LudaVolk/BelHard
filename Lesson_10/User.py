"""
Добавить в класс User из прошлого дз следующий функционал:
	- сохранение всей информации о пользователя в базе данных
	- изменение инфорамации о пользователе с сохранением изменений в базе данных
	- загрузка  информации о пользователе из базы данных и вывод ее на экран используя логин
	- вывод на экран информации о всех пользователях из базы данных
	* вывод на экран всех пользователей с активной подпиской
	* вывод на экран пользователей у которых подписка заканчивается в течении 10 дней
"""

import sqlite3

con = sqlite3.connect('TestDataBase.db')
cur = con.cursor()

class User:
    name: str
    login: str
    password: str

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    # def user_delete(self):
    #     sql = "DELETE FROM Users"
    #     with con:
    #         # q = cur.execute(sql)
    #         print(cur.execute(sql).fetchall())

    def user_save(self):
        sql = "UPDATE users SET password = 'q999' WHERE name = 'Luda' AND login = 'luda456'"
        with con:
            q = cur.execute(sql)

    def user_add(self):
        sql = f"INSERT INTO Users (name, login, password)"\
            f"VALUES ('{self.name}', '{self.login}', '{self.password}')"
        with con:
            q = cur.execute(sql)

    def connect_db(self):
        base = ()
        data = dict(
            name=self.name,
            login=self.login,
            password=self.password
        )
        # with base as b:
        #     user_count = b.cursor.exe(f"SELECT * FROM users WHERE login = '{self.login}'")
        # if user_count:
        #     b.update("users", data, f"login = '{self.login}")
        # else:
        #     b.insert("users", data)

    def get_login_inf(self):
        with con:
             cur.execute(f"SELECT * FROM users WHERE login = '{self.login}'")
             while True:
                row = cur.fetchone()

                if row == None:
                    break
                print(row[0], row[1], row[2], row[3])

try:
    user1 = User("Luda", "luda456", "lll222")
    user2 = User("Lena", "lena789", "eee333")
    user3 = User("Dima", "dima123", "ddd111")
except:
    print("Error")
else:
    user1.connect_db()
    user1.user_add()
    # user2.user_add()
    # user3.user_add()
    # user1.user_save()
    user2.get_login_inf()

    print("________________")

import sqlite3 as lite

con = lite.connect('TestDataBase.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Users")
    while True:
        row = cur.fetchone()

        if row == None:
            break
        print(row[1], row[2], row[3])