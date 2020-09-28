class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Поехали'

    def stop(self):
        return 'Стоп'

    def turn(self, direction):
        return f'Поворот {direction}'

    def show_speed(self):
        return f'Скорость {self.speed}'


class TownCar(Car):
    __speed_limit = 60

    def show_speed(self):
        if self.speed > self.__speed_limit:
            return f'Скорость {self.speed}. Превышение скорости'
        else:
            return f'Скорость {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    __speed_limit = 40

    def show_speed(self):
        if self.speed > self.__speed_limit:
            return f'Скорость {self.speed}. Превышение скорости'
        else:
            return f'Скорость {self.speed}'


class PoliceCar(Car):
    pass


car1 = TownCar(60, 'red', 'bibika', 0)
print(car1.name)
print(car1.color)
print(car1.speed)
print(car1.is_police)
print(car1.show_speed())
print(car1.go())
print(car1.stop())
print(car1.turn('налево'))
print(car1.turn('направо'))

car2 = PoliceCar(100, 'white', 'police car', 1)
print(car2.name)
print(car2.color)
print(car2.speed)
print(car2.is_police)
print(car2.show_speed())
print(car2.go())
print(car2.stop())
print(car2.turn('налево'))
print(car2.turn('направо'))

car3 = WorkCar(60, 'black', 'traktor', 0)
print(car3.name)
print(car3.color)
print(car3.speed)
print(car3.is_police)
print(car3.show_speed())
print(car3.go())
print(car3.stop())
print(car3.turn('налево'))
print(car3.turn('направо'))
