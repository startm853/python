from itertools import zip_longest


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.gen_matrix(self.data)

    def __add__(self, other):
        res = []
        for i, j in zip_longest(self.data, other.data, fillvalue=[0]):
            tmp = []
            for a, b in zip_longest(i, j, fillvalue=0):
                tmp.append(a + b)
            res.append(tmp)
        return self.gen_matrix(res)

    def gen_matrix(self, lists):
        res = ''
        for s, items in enumerate(lists, 1):
            for i, item in enumerate(items, 1):
                res += str(item)
                res += '\t' if i < len(items) else \
                    '\n' if s < len(lists) else ''
        return res


try:
    print(Matrix([[31, 22], [27, 43], [51, 86]]))
    print()
    print(Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]]))
    print()
    print(Matrix([[3, 5, 8, 3], [8, 3, 7, 1]]))
    print()
    print('Сумма одноразмерных:')
    print(Matrix([[1, 2], [3, 4]]) + Matrix([[5, 6], [7, 8]]))
    print()
    print('Сумма разноразмерных:')
    print(Matrix([[1, 2], [3, 4]]) + Matrix([[5, 6], [7, 8], [4, 5]]))
    print()
    print('Сумма разноразмерных:')
    print(Matrix([[1, 2, 4], [3, 4, 0], [12, 52, 7]]) + Matrix([[5, 6], [7, 8], [-11, -2]]))
except Exception as e:
    print(e)
