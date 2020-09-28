class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        self.title = 'Pen'
        print(f'This is {self.title}!')


class Pencil(Stationery):
    def draw(self):
        self.title = 'Pencil'
        print(f'This is {self.title}!')


class Handle(Stationery):
    def draw(self):
        self.title = 'Handle'
        print(f'This is {self.title}!')


item1 = Stationery()
item1.draw()

item2 = Pen()
item2.draw()

item3 = Pencil()
item3.draw()

item4 = Handle()
item4.draw()
