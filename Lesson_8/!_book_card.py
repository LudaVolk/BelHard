"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date
CURRENT_YEAR = date.today().year

class BookCard():
    authors: str
    title: str
    year: int

    def __init__(self, authors: str, title: str, year: int):
         self.__authors = authors
         self.__title = title
         self.__year = year

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        try:
            if isinstance(authors, int):
                raise ValueError('!')
        except ValueError:
                print('ValueError')
                #exit(0)
                return
        self.__authors = authors

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        try:
            if isinstance(title, int):
                raise ValueError('!')
        except ValueError:
            print('ValueError')
            #exit(0)
            return
        self.__title = title

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        try:
            if isinstance(year, str):
                raise NameError('!')
        except NameError:
            print('Error')
            #exit(0)
            return
        self.__year = year

    def __repr__(self):
        return repr((self.__authors, self.__title, self.__year))

    def __str__(self):
        return str(self.__dict__)

books = [BookCard(b[0], b[1], b[2]) for b in [
     ("Hello", ["Volkov"], -2001),
     ("Hi Hi", ["Petrov"], 2026),
     ("ABC", ["Resto"], 1975),
     ("Norma", ["Ivanov"], 1999),
     ("ABC", ["Ivanov"], 2020),
     ("TTT", ["Volkov"], -1),
     ("Nith", ["Ludmila"], 1979),
     ("Class", ["Resto"], 2030),
     ("Hi all", ["Petrov"], 2002),
     ("The good day", ["Sidorov"], 1916)]]

def select_by_year(books, year):
     test = []
     for b in books:
         if b.year <= CURRENT_YEAR and b.year > 0:
             test.append(b)
     return test
books = select_by_year(books, CURRENT_YEAR)

test2 = []
test2 = sorted(books, key=lambda BookCard: BookCard.year)
for t in test2:
    print(t)
#print(sorted(books, key=lambda BookCard: BookCard.year)) в строке

test2[0].year = 'ooooo'
test2[0].authors = 1111
test2[0].title = 1111

