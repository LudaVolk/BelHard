r"""
Напишите функцию, которая по заданной текстовой строке (возможно, с пунктуацией и разрывами строк) возвращает массив из трех самых часто встречающихся слов в порядке убывания количества вхождений.
		Слово представляет собой строку букв русского или латинского алфавита, необязательно содержащую один или несколько апострофов ( ').
		Апострофы могут стоять в начале, середине или конце слова ( допустимы все 'abc, abc', 'abc', )ab'c
		Любые другие символы (например #, \, , /, ....) не являются частью слова и должны рассматриваться как пробелы.
		Совпадения должны быть нечувствительны к регистру, а слова в результате должны быть в нижнем регистре.
		Если текст содержит менее трех уникальных слов, то должны быть возвращены либо первые 2, либо первое 1 слово, либо пустой массив, если текст не содержит слов


"""

import re
from collections import Counter
#1й
frequency = {}

document_text = """ С помощью модуля Python это сделать очень просто. 
Python cначала нужно импортировать класс datetime из модуля datetime, 
после чего создать объект datetime Python. Модуль предоставляет метод now(), 
который возвращает текущие дату и время с учетом локальных настроек now Python  
"""

text_string = document_text.lower()
match_pattern = re.findall(r"[а-я']*[а-яa-z]+[a-z']*", text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

count2 = 0
for words in frequency_list:
    count2 = count2 + 1
    if count2 > 3:
        break
print(words, frequency[words])

sorted_by_second = sorted(frequency_list, key=lambda words: frequency[words], reverse=True)
print(sorted_by_second)

#2й
def top_3_words(text):
    words = re.findall(r"[а-я']*[а-яa-z]+[a-z']*", text.lower())
    top_3 = Counter(words).most_common(3)
    return [typ[0] for typ in top_3]

text = """ С помощью модуля Python это сделать очень просто. 
Python cначала нужно импортировать класс datetime из модуля datetime, 
после чего создать объект datetime Python. Модуль предоставляет метод now(), 
который возвращает текущие дату и время с учетом локальных настроек now Python  
"""
print(top_3_words(text))

#3й
top_3_words3 = lambda t: [w for w, c in Counter (re.findall(r"[а-я']*[а-яa-z]+[a-z']*", text.lower())).most_common(3)]

print(top_3_words3(text))