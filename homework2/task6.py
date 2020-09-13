# Items

text = ('-' * 50) + '\nВыберите действие:\n1 - Добавить товары\n2 - Удалить товары\n\
3 - Изменить товар\n4 - Список товаров\n5 - Аналитика\n6 - Пойди домой\n'

column = ['название', 'цена', 'количество', 'ед']

items = []

# Данные для теста
# компьютер2;20001;7;шт.
# принтер;6000;2;шт.
# сканер;2000;7;шт.
#
# items = [
#     (1, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'}),
#     (2, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
#     (3, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'})
# ]


while True:
    action = input(text)
    if action == '1':
        count = int(input('Укажите количество новых товаров\n'))
        if count > 0:
            print('Укажите данные товара в CSV (разделитель ;). Каждый с новой строки\n')
            while count > 0:
                new_item = input().split(';')
                item = {}
                for i in enumerate(new_item):
                    key = i[0]
                    value = i[1]
                    if column[key] == 'цена' or column[key] == 'количество':
                        value = int(value)
                    item.update({column[key]: value})
                if len(items) == 0:
                    items.append(tuple([len(items) + 1, item]))
                else:
                    items.append(tuple([items[len(items) - 1][0] + 1, item]))
                add_text = ''
                count -= 1

    if action == '2':
        del_items = input('Укажите ID товаров через запятую\n').replace(', ', ',').replace(' ,', ',').split(',')
        deleted = []
        for d in del_items:
            int_d = int(d)
            for item in items:
                if int_d in item:
                    deleted.append(int_d)
                    items.remove(item)
        print(f'Товары {deleted} удалены\n' if len(deleted) > 0 else 'Не найдено совпадений ID\n')

    if action == '3':
        edit = int(input('Укажите ID изменяемого товара\n'))
        for item in items:
            if edit in item:
                new_value = input('Укажите новые параметры в CSV\n').split(';')
                print(new_value)
                for val in enumerate(new_value):
                    key = val[0]
                    value = val[1]
                    if column[key] == 'цена' or column[key] == 'количество':
                        value = int(value)
                    items[1][1][column[key]] = value
            else:
                print('Товар с таким ID не найден\n')

    if action == '4':
        print(f'Список товаров\n')
        if len(items) > 0:
            for item in items:
                print(item)
        else:
            print('В базе нет товаров\n')

    if action == '5':
        analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
        for item in items:
            analytics['название'].append(item[1]['название'])
            analytics['цена'].append(item[1]['цена'])
            analytics['количество'].append(item[1]['количество'])
            analytics['ед'].append(item[1]['ед'])
        print(analytics)
    if action == '6':
        break
