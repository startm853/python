import os


def get_data(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = {}
            for s in f.readlines():
                subject, lections, practice, laboratory = s.split()
                subject = subject.strip(':')
                summa = num_from_string(lections) + num_from_string(practice) + num_from_string(laboratory)
                data.update({subject: summa})
            return data
    except IOError:
        return 'Ошибка ввода-вывода'


def num_from_string(string):
    """

    :param string: На входе строки вида: '-', '30(пр)', '-\n'
    :return: Вырезанные цифры из строки, приведенные к int, или 0, если в строке не было ни одной цифры
    """
    return int(''.join([num for num in filter(lambda num: num.isnumeric(), string)])) if ''.join(
        [num for num in filter(lambda num: num.isnumeric(), string)]) != '' else 0


filename = 'text_6.txt'
if os.path.exists(filename):
    print(get_data(filename))
else:
    print(f'Файл {filename} не существует')
