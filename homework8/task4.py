class Stock:
    """
    Все созданные в рамках объекта склада элементы хранятся в __items.
    Складов может быть несколько, такая логика хранения позволит масштабироваться
    """
    __items = []

    def get_items(self, device=None, dep=None):
        items = None
        if dep:
            items = [*[self.__get_printer(item) for item in self.__items if
                       item.departament == dep and item.device == 'printer'],
                     *[self.__get_scanner(item) for item in self.__items if
                       item.departament == dep and item.device == 'scanner'],
                     *[self.__get_mfu(item) for item in self.__items if
                       item.departament == dep and item.device == 'mfu']]
        else:
            if device == 'printer':
                items = [self.__get_printer(item) for item in self.__items if item.device == device]
            elif device == 'scanner':
                items = [self.__get_scanner(item) for item in self.__items if item.device == device]
            elif device == 'mfu':
                items = [self.__get_mfu(item) for item in self.__items if item.device == device]
        return items

    def add(self, device):
        try:
            article = self.new_article()
            if device[0] == 'printer':
                new_object = self.__add_printer(device, article)
            elif device[0] == 'scanner':
                new_object = self.__add_scanner(device, article)
            elif device[0] == 'mfu':
                new_object = self.__add_mfu(device, article)
            else:
                return 'Некорректный тип устройства'
            if isinstance(new_object, str):
                return new_object
            self.__items.append(new_object)
            return 'Добавлено'
        except Exception as e:
            return f'Ошибка при добавлении {e}'

    def new_article(self):
        """

        :return: уникальный ID нового устройства
        """
        article = self.__items[-1].article + 1 if len(self.__items) > 0 else 1
        return article

    @staticmethod
    def __add_printer(device, article):
        device, brand, departament, colors, paper_format = device
        if not validate(dep=departament):
            return 'Ошибка валидации. Некорректный офис'
        if not validate(colors=colors):
            return 'Ошибка валидации. Некорректный цвет'
        if not validate(paper_format=paper_format):
            return 'Ошибка валидации. Некорректный формат бумаги'
        return Printer(article, device, brand, departament, colors, paper_format)

    @staticmethod
    def __get_printer(obj):
        return obj.article, obj.device, obj.brand, obj.departament, obj.colors, obj.paper_format

    @staticmethod
    def __add_scanner(device, article):
        device, brand, departament, type, paper_format = device
        if not validate(dep=departament):
            return 'Ошибка валидации. Некорректный офис'
        if not validate(type=type):
            return 'Ошибка валидации. Некорректный тип сканирования'
        if not validate(paper_format=paper_format):
            return 'Ошибка валидации. Некорректный формат бумаги'
        return Scanner(article, device, brand, departament, type, paper_format)

    @staticmethod
    def __get_scanner(obj):
        return obj.article, obj.device, obj.brand, obj.departament, obj.type, obj.paper_format

    @staticmethod
    def __add_mfu(device, article):
        device, brand, departament, print_technology = device
        if not validate(dep=departament):
            return 'Ошибка валидации. Некорректный офис'
        if not validate(print_technology=print_technology):
            return 'Ошибка валидации. Некорректная технология печати'
        return Mfu(article, device, brand, departament, print_technology)

    @staticmethod
    def __get_mfu(obj):
        return obj.article, obj.device, obj.brand, obj.departament, obj.print_technology

    def update(self, id):
        """

        :param id: ID устройство, которое обновляем. Изменить можно только департамент
        :return: Возващает статус операции обновления в понятном для пользователя виде
        """
        items = [*[item for item in self.__items if item.device == 'printer' and item.article == id],
                 *[item for item in self.__items if item.device == 'scanner' and item.article == id],
                 *[item for item in self.__items if item.device == 'mfu' and item.article == id]]
        print('Для устройства можно изменить только атрибут Departament')
        i = input('Выберите, на что меняем:\n[0] - Склад,\n[1-3] - Офисы\n[4] - Списание\n')
        if i in '01234':
            if i == '0':
                s = 'Склад'
            elif i > '0' and i < '4':
                s = f'Офис {i}'
            elif i == '4':
                s = 'Списанный'
            if s:
                items[0].departament = s
                return 'Данные обновлены'
        return 'Ошибка. Вы указали несуществующий офис'


class OfficeEquipment:
    def __init__(self, article, device, brand, departament):
        self.device = device
        self.brand = brand
        self.departament = departament
        self.article = article

    def update(self, departament):
        self.departament = departament


class Printer(OfficeEquipment):
    def __init__(self, article, device, brand, departament, colors, paper_format):
        super().__init__(article, device, brand, departament)
        self.colors = colors
        self.paper_format = paper_format


class Scanner(OfficeEquipment):
    def __init__(self, article, device, brand, departament, type, paper_format):
        super().__init__(article, device, brand, departament)
        self.type = type
        self.paper_format = paper_format


class Mfu(OfficeEquipment):
    def __init__(self, article, device, brand, departament, print_technology):
        super().__init__(article, device, brand, departament)
        self.print_technology = print_technology


def validate(dep=None, colors=None, paper_format=None, type=None, print_technology=None):
    """
    Скрипт валидирует все входящие параметры из CSV

    :param dep: Департамент
    :param colors: Цветной/Чернобелый
    :param paper_format: Формат бумаги
    :param type: Тип устройства сканера
    :param print_technology: Технология печати
    :return: True/False в зависимости от прохождения валидации
    """
    if dep:
        departaments = ['Склад', 'Офис 1', 'Офис 2', 'Офис 3', 'Списанный']
        if dep in departaments:
            return True
    if colors:
        if colors in '01':
            return True
    if paper_format:
        formats = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
        if paper_format in formats:
            return True
    if type:
        types = ['Планшетный', 'Протяжный', 'Фотоаппаратный', 'Слайд-сканер']
        if type in types:
            return True
    if print_technology:
        tech = ['Лазерное', 'Светодиодное', 'Струйное']
        if print_technology in tech:
            return True
    return False


types = {
    '1': 'printer',
    '2': 'scanner',
    '3': 'mfu'
}

stock = Stock()

#  Тестовые данные
data = [
    ['printer', 'Xerox Phaser 3020BI', 'Склад', '', 'A4'],
    ['printer', 'Canon i-SENSYS LBP623Cdw', 'Офис 1', '', 'A4'],
    ['printer', 'HP LaserJet Pro M15w', 'Офис 2', '', 'A4'],
    ['printer', 'HP Laser 107w', 'Офис 3', '', 'A4'],
    ['printer', 'Epson L120', 'Склад', '1', 'A4'],
    ['printer', 'Canon PIXMA iP8740', 'Офис 1', '1', 'A3'],
    ['printer', 'Epson L1800', 'Офис 2', '1', 'A3'],
    ['printer', 'Canon PIXMA PRO-10S', 'Списанный', '1', 'A3'],
    ['scanner', 'Canon CanoScan LiDE 400', 'Склад', 'Планшетный', 'A4'],
    ['scanner', 'Canon CanoScan LiDE 300', 'Склад', 'Планшетный', 'A4'],
    ['scanner', 'Brother ADS-1200', 'Офис 1', 'Протяжный', 'A4'],
    ['scanner', 'DOKO X08A3', 'Офис 1', 'Фотоаппаратный', 'A3'],
    ['scanner', 'Epson WorkForce DS-1630', 'Офис 1', 'Планшетный', 'A4'],
    ['scanner', 'Plustek OpticFilm 8200i SE', 'Офис 2', 'Слайд-сканер', ''],
    ['scanner', 'Canon imageFORMULA DR-C225', 'Офис 2', 'Протяжный', 'A4'],
    ['scanner', 'Epson Perfection V600 Photo', 'Офис 3', 'Планшетный', 'A4'],
    ['mfu', 'HP LaserJet Pro MFP M28w', 'Склад', 'Лазерное'],
    ['mfu', 'Xerox WorkCentre 3025BI', 'Склад', 'Лазерное'],
    ['mfu', 'Brother DCP-L2520DWR', 'Склад', 'Лазерное'],
    ['mfu', 'Ricoh SP C360SFNw', 'Офис 1', 'Светодиодное'],
    ['mfu', 'Brother MFC-L3770CDW', 'Офис 3', 'Лазерное'],
    ['mfu', 'Canon PIXMA G3411', 'Офис 3', 'Струйное'],
    ['mfu', 'HP DeskJet Ink Advantage 5075 M2U86C', 'Офис 3', 'Струйное'],
    ['mfu', 'HP Smart Tank 515', 'Списанный', 'Струйное']
]

for item in data:
    stock.add(item)


def get_device():
    print('-' * 50)
    device = []
    action = input(
        '[1] - Посмотреть склад\n[2] - Посмотреть устройства по офису\n[3] - Посмотреть устройства по типу\n[*] - Вернуться на уровень выше\n')
    if action == '1':
        device = stock.get_items(data, dep='Склад')
        print('Устройства на складе:')
    elif action == '2':
        office = input('Выберите офис: [1], [2], [3], [4] - списанные\n')
        if office in '1234':
            office = 'Офис ' + office if office < '4' else 'Списанный'
            device = stock.get_items(data, office)
            print(f'Устройства {office}:')
        else:
            print('Нет такого офиса')
    elif action == '3':
        device_type = input('Выберите устройство:\n[1] - printer\n[2] - scanner\n[3] - mfu\n')
        if device_type in types:
            device = stock.get_items(device=types[device_type])
        else:
            print('Нет такого устройства')
    else:
        return True
    for i in device:
        print(i)
    print('-' * 50)


def add_device():
    """
    Примеры для добавления элементов
    Принтер: printer;Canon PIXMA TS304;Склад;1;A4
    Сканер: scanner;Plustek MobileOffice S410;Склад;Протяжный;A4
    МФУ: mfu;Epson L4160;Склад;Струйное
    :return:
    """
    print('-' * 50)
    print('Добавляем устройство.')
    device_type = input(
        'Выберите тип добавляемого устройства\n[1] - printer\n[2] - scanner\n[3] - mfu\n[*] - Вернуться на уровень выше\n')
    if device_type in '123':
        print('Введите в формате CSV (разделитель ;) данные об устройстве')
        new_device = None
        print('Необходимые данные: ', end='')
        if types[device_type] == 'printer':
            new_device = input('device, brand, departament, colors, paper_format\n').split(';')
        elif types[device_type] == 'scanner':
            new_device = input('device, brand, departament, type, paper_format\n').split(';')
        elif types[device_type] == 'mfu':
            new_device = input('device, brand, departament, print_technology\n').split(';')
        if new_device:
            res = stock.add(new_device)
            print(res)
    else:
        print('Нет такого устройства')


def update_device():
    print('-' * 50)
    print('Обновляем устройство.')
    try:
        id = int(input('Укажите ID обновляемого устройства\n'))
        res = stock.update(id)
        print(res)
    except Exception as e:
        print(f'Ошибка: {e}')


while True:
    action = input(
        '[1] - Посмотреть базу\n[2] - Добавить новое устройство\n[3] - Обновить устройство / Списать устройство\n[*] - Выход\n')
    if action == '1':
        get_device()
    elif action == '2':
        add_device()
    elif action == '3':
        update_device()
    else:
        break
