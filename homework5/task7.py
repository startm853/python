import json
import os


def get_data(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = {}
            for s in f.readlines():
                company, form, income, costs = s.split()
                data.update({company: {'form': form, 'income': float(income), 'costs': float(costs)}})
            return data
    except IOError:
        print('Ошибка ввода-вывода')


def avg_income(companies):
    result, avg, k = {}, 0, 0
    for i in companies:
        dif = companies[i]['income'] - companies[i]['costs']
        result.update({i: dif})
        if dif > 0:
            avg += dif
            k += 1
    return [result, {'average_profit': round(avg / k, 2)}]


def generate_file(file, data):
    try:
        with open(file, 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f'Файл {file} создан/перезаписан')
    except IOError:
        print('Ошибка ввода-вывода')


filename = 'text_7.txt'
if os.path.exists(filename):
    companies = get_data(filename)
    json_file = 'text_7.json'
    while True:
        v = input('[1] - Вывести список всех компаний\n[2] - Подсчет средней прыбилы по компаниям с доходом\n\
[3] - Записываем результат в json\n[*] - Выход\n')
        if v == '1':
            print(companies)
        elif v == '2':
            try:
                print(avg_income(companies))
            except TypeError:
                print('Переменная companies получила не получила ожидаемый формат данных')
        elif v == '3':
            try:
                generate_file(json_file, avg_income(companies))
            except TypeError:
                print('Переменная companies получила не получила ожидаемый формат данных')
        else:
            break
else:
    print(f'Файл {filename} не существует')
