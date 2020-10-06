class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


print("Введите значение. Для выхода введите 'stop'")
res = []
while True:
    try:
        number = input()
        if number == 'stop':
            break
        for n in number:
            if n not in '1234567890':
                raise OwnError('Введенное значение не является числом')
        res.append(int(number))
    except Exception as e:
        print('Ошибка:', e)
print(res)
