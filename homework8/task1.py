import time


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, d):
        if Date.validator(d):
            day, month, year = list(map(int, d.split('-')))
            return cls(day, month, year)
        return False

    @staticmethod
    def validator(date):
        try:
            time.strptime(date, '%d-%m-%Y')
            return True
        except ValueError:
            return False


d_1 = Date.set_date('01-12-2020')
print(d_1.year, d_1.month, d_1.day) if d_1 else print('Invalid date. Format: dd-mm-YYYY')
print()
d_2 = Date.set_date('31-02-2020')
print(d_2.year, d_2.month, d_2.day) if d_2 else print('Invalid date. Format: dd-mm-YYYY')
