class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        raise OwnError('Нельзя просто так взять и разделить на 0')
    print(a / b)
except Exception as e:
    print('Ошибка:', e)
