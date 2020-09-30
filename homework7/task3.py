class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return abs(self.cell - other.cell)

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        if other.cell == 0:
            return 0
        return self.cell // other.cell

    def make_order(self, rows):
        if rows < 1:
            print('Должна быть минимум 1 клетка в строке')
            rows = 1
        res = ''
        for i in range(1, self.cell + 1):
            res += '*\n' if i % rows == 0 else '*'
        return res


cell_1 = Cell(3)
cell_2 = Cell(7)

print('Сумма:', cell_1 + cell_2)
print('Разница по модулю:', cell_1 - cell_2)
print('Умножение', cell_1 * cell_2)
print('Целочислененое деление', cell_1 // cell_2)
print()

cell_3 = Cell(14)
print(cell_3.make_order(5))
