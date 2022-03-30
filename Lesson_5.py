def calculate():
    i = 0
    while True:
        i = i + 1
        print('цикл', i)
        try:
            number_1 = float(input('Введите первое число: '))
            operation = input('Выполните операцию:  ')
            number_2 = float(input('Введите второе число: '))
            if str(operation.upper()) == "СТОП":
                print(f"стоп = Завершение цикла")
                break
        except ValueError:
            print('Некорректный тип данных')
            continue
        except UnboundLocalError:
            print('Операция введена некорректно')
            continue
        except NameError:
            print('Некорректный тип данных')
            continue
        if operation == '+':
            try:
                print('{} + {} = '.format(number_1, number_2))
                print(number_1 + number_2)
                break
            except UnboundLocalError:
                print('Некорректный ввод +')
            continue
        elif operation == '-':
            try:
                print('{} - {} = '.format(number_1, number_2))
                print(number_1 - number_2)
                break
            except UnboundLocalError:
                print('Некорректный ввод -')
            continue
        elif operation == '*':
            try:
                print('{} * {} = '.format(number_1, number_2))
                print(number_1 * number_2)
                break
            except UnboundLocalError:
                print('Некорректный ввод *')
            continue
        elif operation == '/':
            try:
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)
                break
            except UnboundLocalError:
                print('Некорректный ввод /')
            except ZeroDivisionError:
                print('деление на 0 недоступно')
            continue
           # return 0
        else:
            print('Повторить снова')
    print('количество выполненных циклов', i)
calculate()
