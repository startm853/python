def generate_file(file):
    try:
        with open(file, 'w+', encoding='utf-8') as f:
            s = input('Введите числа через пробел:\n')
            try:
                list(map(float, s.split()))  # Валидация ввода
                print(s, file=f)
                print(f'Файл {file} создан/перезаписан')
            except ValueError:
                print('Можно вводить только числа')
    except IOError:
        print('Ошибка ввода-вывода')


def get_data(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = list(map(float, f.read().strip('\r\n').split()))
            return data
    except FileNotFoundError:
        print(f'Файл {file} не существует')
    except IOError:
        print('Ошибка ввода-вывода')


filename = 'text_5.txt'
while True:
    v = input('[1] - Создать файл\n[2] - Посчитать сумму для данных в файле\n[*] - Выход\n')
    if v == '1':
        generate_file(filename)
    elif v == '2':
        numbers = get_data(filename)
        try:
            print(round(sum(numbers), 2))
        except TypeError:
            print('Переменная numbers получила не получила ожидаемый формат данных')
    else:
        break
