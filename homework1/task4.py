# maximum

number = int(input('Введите число\n'))

maximum = 0
while True:
    n = number % 10
    number = number // 10
    if maximum < n:
        maximum = n
    if maximum == 9 or number == 0:
        break

print(maximum)
