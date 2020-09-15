def sum_max(a, b, c):
    return round(a + b + c - min(a, b, c), 2)


while True:
    try:
        a = float(input('Введите первое число:\n'))
        b = float(input('Введите второе число:\n'))
        c = float(input('Введите третье число:\n'))
        print(f'Результат: {sum_max(a, b, c)}')
    except ValueError:
        print(f'Необходимо вводить числа')
    finally:
        again = input(f"{'-' * 50}\n[Q] - выход\n[Enter] - попробовать еще раз\n")
        if again.lower() == 'q':
            break
