from itertools import count, cycle, repeat, takewhile


def a():
    try:
        c = int(input('Введите первое число последовательности:\n'))
        # Ввариант 1
        res = []
        for el in count(c):
            if el > 50:
                break
            else:
                res.append(el)
        print(res)

        res = []
        # Ввариант 2
        for el in takewhile(lambda x: x <= 50, count(c)):
            res.append(el)
        print(res)
    except ValueError:
        print('Необходимо ввести число')


def b():
    input_list = ['abc', '123', 'zxc', '789']
    # Ввариант 1
    c = 0
    res = ''
    for el in cycle(input_list):
        if c >= 40:
            break
        res = res + el
        c += 1
    print(res)

    # Ввариант 2
    res = ''
    for el in repeat(input_list, 10):
        for letter in el:
            res = res + letter
    print(res)


i = input('Что делаем?\n[1] - Итератор чисел\n[2] - Итератор списка\n')
if i == '1':
    a()
elif i == '2':
    b()
else:
    print('You shall not pass')
