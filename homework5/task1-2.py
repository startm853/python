def generate_file(file):
    try:
        with open(file, 'w+', encoding='utf-8') as f:
            print('Введите построчно содержимое файла')
            while True:
                s = input('')
                if s == '':
                    break
                print(s, file=f)
            print(f'Файл {file} создан/перезаписан')
    except IOError:
        print('Ошибка ввода-вывода')


def count_str_words(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            counts = {}
            for n, s in enumerate(f.readlines(), 1):
                counts.update({n: len(s.split())})
            for i in counts:
                print(f'Строка {i} - Слов {counts[i]}')
    except FileNotFoundError:
        print(f'Файл {file} не существует')
    except IOError:
        print('Ошибка ввода-вывода')


filename = "task1.txt"
while True:
    v = input('[1] - Создать файл\n[2] - Посчитать количество строк и слов в строках\n[*] - Выход\n')
    if v == '1':
        generate_file(filename)
    elif v == '2':
        count_str_words(filename)
    else:
        break
