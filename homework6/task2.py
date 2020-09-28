class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mas(self):
        return f'{round(self._length * self._width * 25 * 5 / 1000, 2)} тонн'


try:
    new_road = Road(10.123, 20)
    print(new_road.mas())
except Exception as e:
    print(e)
