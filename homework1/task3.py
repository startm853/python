# Sum Like JavaScript

# Вариант 1
print('------------Вариант 1------------')
n = input('Введите n\n')
number1 = int(n)
number2 = int(n + n)
number3 = int(n + n + n)

print(number1 + number2 + number3)

# Ниже сделал чуть сложнее, чем описано в задании:
# количество слагаемых задается пользователем. К каждому последующему слагаемому будет добавлена еще одна n

# Вариант 2
print('------------Вариант 2------------')
n = int(input('Введите n\n'))

# Считаем длину входного значения
length_N = 1
len_input = n // 10
while len_input > 1:
    length_N += 1
    len_input = len_input // 10

while True:
    count = int(input('Введите количество слагаемых\n'))
    i = 1
    summa = 0
    number = ''
    while i <= count:
        number = number + str(n)
        if i == count:
            summa = summa + int(number)
            count -= 1
            i = 1
            number = ''
            continue
        i += 1
    break
print(f'{summa:,}')
