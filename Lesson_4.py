from num2words import num2words
while True:
    number_1 = float(input('Введите первое число: '))
    operation = input("Введите операцию (+,-,/,*) :")
    number_2 = float(input('Введите второе число: '))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        a = (round(number_1 + number_2))
        break
   # print(num2words(a, lang='ru'))
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        a = (round(number_1 - number_2))
        break
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        a = (round(number_1 * number_2))
        break
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        a = (round(number_1 * number_2))
        break
    else:
        print('Повторить операцию')
print(num2words(a, lang='ru'))
