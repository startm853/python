def fact(n):
    for i in (range(1, n + 1)):
        yield i


try:
    f = 1
    n = int(input('Введите число:\n'))
    if n >= 0:
        for el in fact(n):
            f = f * el
        print(f'Факториал равен: {f}')
    else:
        print('Факториал можно расчитать только для неотрицательнх целых чисел')
except ValueError:
    print('Можно ввести только число')
