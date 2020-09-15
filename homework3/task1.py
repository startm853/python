def division(d1, d2):
    try:
        res = round(d1 / d2, 2)
    except ZeroDivisionError:
        res = 'Не хочу делить на 0'
    return res


while True:
    try:
        a = float(input('Введите первое число:\n'))
        b = float(input('Введите второе число:\n'))
        print(f'Результат: {division(a, b)}')
    except ValueError:
        print(f'Необходимо вводить числа')
    finally:
        again = input(f"{'-' * 50}\n[Q] - выход\n[Enter] - попробовать еще раз\n")
        if again.lower() == 'q':
            break
