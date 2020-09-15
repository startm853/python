def custom_summa(data):
    res = 0
    for i in data:
        try:
            res = res + float(i)
        except ValueError:
            print(f'Введенное значение {i} было проигнорировано')
        finally:
            if i == 'q':
                break
    return round(res, 2)


summa = 0
while True:
    data = [i.lower() for i in input('Введите числа для суммирования\n').split()]
    add = custom_summa(data)
    summa = round(summa + add, 2)
    print(f'{summa} ({add})')
    if 'q' in data:
        break
    again = input(f"{'-' * 50}\n[Q] - выход\n[Enter] - попробовать еще раз\n")
    if again.lower() == 'q':
        break
