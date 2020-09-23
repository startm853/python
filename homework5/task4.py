from googletrans import Translator
import os


def get_words(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = {}
            for s in f.readlines():
                left, right = s.split(' - ')
                data.update({right.strip('\r\n'): left})
            return data
    except IOError:
        print('Ошибка ввода-вывода')


def eng_to_rus(data):
    translator = Translator()
    result = {}
    for i in data:
        result.update({i: translator.translate(data[i], src='en', dest='ru').text})
    return result


def generate_file(file, data):
    try:
        with open(file, 'w+', encoding='utf-8') as f:
            for i in data:
                print(f'{data[i]} - {i}', file=f)
        print(f'Результат записан в файл: {file}')
    except IOError:
        print('Ошибка ввода-вывода')


filename = 'text_4.txt'
if os.path.exists(filename):
    words = get_words(filename)
    try:
        new_words = eng_to_rus(words)
        new_filename = 'text_4_new.txt'
        generate_file(new_filename, new_words)
    except TypeError:
        print('Переменная words получила не получила ожидаемый формат данных')
else:
    print(f'Файл {filename} не существует')
