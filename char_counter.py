"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
#пробую первый раз
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char:
            count = count + 1
        index = index + 1
    return count
    while index < len(string):
        if string[index] == char:
            count = count + 1
        index = index + 1
    return count
STR_VAL = 'python is the fastest-growing major programming language'
print("'p': ", (count_chars(STR_VAL, 'p')))
print("'y': ", (count_chars(STR_VAL, 'y')))


# пробую 2й раз
def count_chars(STR_VAL):
    letters = set(STR_VAL)
    a = {}
    for letter in letters:
        a[letter] = STR_VAL.count(letter)
    return a
STR_VAL = 'python is the fastest-growing major programming language'
print(count_chars(STR_VAL))