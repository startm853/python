import os


def get_workers(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = []
            for s in f.readlines():
                name, salary = s.split()
                data.append([name, float(salary)])
            return data
    except FileNotFoundError:
        print(f'Файл {file} не существует')
    except IOError:
        print('Ошибка ввода-вывода')


def less_20k(data):
    lowest = []
    for name, salary in data:
        if salary < 20000:
            lowest.append(name)
    return f'Оклад менее 20к у сотрудников: {lowest}'


def avg_salary(data):
    summa = 0
    for _, salary in data:
        summa += salary
    return f'Средний доход сотрудников: {round(summa / len(data), 2)}'


filename = 'text_3.txt'
if os.path.exists(filename):
    workers = get_workers(filename)
    try:
        print(less_20k(workers))
        print(avg_salary(workers))
    except TypeError:
        print('Переменная workers получила не получила ожидаемый формат данных')
else:
    print(f'Файл {filename} не существует')
