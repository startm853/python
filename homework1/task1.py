# Calculator

text_argument1 = 'Введите первый аргумент\n'
text_argument2 = 'Введите первый аргумент\n'

while True:
    operation = input('Введите операцию:\n+ - сложение\n- - вычитание\n/ - деление\n* - умножение\n')
    if operation == '+':
        while True:
            count = int(input('Количество слагаемых?\n'))
            if count > 1:
                summa = 0
                i = 1
                str_numbers = ''
                while i <= count:
                    number = float(input(f'Введите слагаемое №{i}\n'))
                    summa = summa + number
                    if str_numbers != '':
                        str_numbers = str_numbers + ' + '
                    str_numbers = str_numbers + str(number)
                    i += 1
                else:
                    print(f'Результат: {str_numbers} = {summa:.2f}')
                break
            else:
                print('Необходимо указать целое число не меньше 2')

    # Не захотел на остальные действия копировать весь код, он почти не поменяется
    elif operation == '-':
        a = float(input(text_argument1))
        b = float(input(text_argument2))
        result = a - b
        print(f'Разность: {result:.2f}')
    elif operation == '/':
        a = float(input(text_argument1))
        b = float(input(text_argument2))
        result = a / b
        print(f'Отношение: {result:.2f}')
    elif operation == '*':
        a = float(input(text_argument1))
        b = float(input(text_argument2))
        result = a * b
        print(f'Произведение: {result:.2f}')
    else:
        print('Что-то пошло не так')
    again = input('Совершить еще операцию? да/нет\n')
    if again == 'да':
        continue
    else:
        break
