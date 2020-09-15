def custom_pow(x, y):
    return round(x ** y, 4)


def custom_pow_2(x, y):
    res = 1 / x
    while y < -1:
        res = res * (1 / x)
        y += 1
    return round(res, 4)


while True:
    try:
        text_error = 'X должен быть положительным числом'
        x = float(input('Введите x:\n'))
        if x <= 0:
            print('X должен быть больше 0')
            continue
        text_error = 'Y должен быть отрицательным целым числом'
        y = int(input('Введите y:\n'))
        if y >= 0:
            print('Y должен быть целым числом меньше 0')
            continue
        print(f'Результат: {custom_pow(x, y)}')
        print(f'Результат: {custom_pow_2(x, y)}')
    except ValueError:
        print(text_error)
    finally:
        again = input(f"{'-' * 50}\n[Q] - выход\n[Enter] - попробовать еще раз\n")
        if again.lower() == 'q':
            break
