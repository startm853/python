# Company Balance

revenue = float(input('Укажите выручку\n'))
expenses = float(input('Укажите издержки\n'))

if expenses < 0:
    expenses = expenses * -1

result = revenue - expenses

if result > 0:
    print(f'Прибыть компании: {result:.2f}')
    profit = result / revenue * 100
    print(f'Рентабельность выручки: {profit:.2f}%')
    workers = int(input('Укажите количество сотрудников\n'))
    print(f'Доход на 1 сотрудника: {result / workers :.2f}')
elif result < 0:
    print(f'Убытки компании: {result:.2f}')
else:
    print('Компания вышла в 0')
