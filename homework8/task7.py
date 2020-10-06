class Complex:
    items = 0

    def __init__(self, i):
        self.i = i

    def __add__(self, other):
        return self.i + other.i

    def __mul__(self, other):
        return self.i * other.i

    @classmethod
    def set_complex(cls):
        try:
            a, b = list(map(float, input(
                f'Создаем объект {cls.__name__} №{Complex.items + 1}. Введите через пробел действительную и мнимую части:\n').split()))
            Complex.items += 1
            return cls(complex(a, b))
        except Exception as e:
            print('Ошибка', e)
            return False


objects = []
while True:
    c = Complex.set_complex()
    if c:
        objects.append(c)
    if len(objects) > 1:
        break

try:
    print('Сложение: ', objects[0] + objects[1])
    print('Произведение: ', objects[0] * objects[1])
except Exception as e:
    print('Ошибка', e)
