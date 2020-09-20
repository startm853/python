from sys import argv


def salary(time, pay, bonus):
    # Премия может быть отрицательной
    return 'Условия ввода: Ставка > 0, Время >= 0' if time < 0 or pay <= 0 else round(time * pay + bonus, 2)


try:
    script, time, pay, bonus = argv
    try:
        print(salary(float(time), float(pay), float(bonus)))
    except ValueError:
        print('Все параметры должны быть числами')
except ValueError:
    print('Должно быть передано 3 параметра: часы, ставка, премия')
