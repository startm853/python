class Worker:
    def __init__(self, name, surname, position, income_wage, income_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(income_wage), "bonus": float(income_bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, income_wage, income_bonus):
        super(Position, self).__init__(name, surname, position, income_wage, income_bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f"{self._income['wage'] + self._income['bonus']}"


def new_worker(name, surname, position, income_wage, income_bonus):
    try:
        return Position(name, surname, position, income_wage, income_bonus)
    except Exception as e:
        print(f'Не получилось создать {name} {surname} {position}.\nError: {e}\n')


def is_obj_exist(obj, func):
    if obj:
        if func == 'get_full_name':
            print(f'Имя: {obj.get_full_name()}')
        if func == 'get_total_income':
            print(f'Доход: {obj.get_total_income()}')


worker1 = new_worker('Вася', 'Пупкин', 'Босс', '100q', 15)
worker2 = new_worker('Алексей', 'Пупкин', 'Босс №2', 100, 10)
worker3 = new_worker('Иван', 'Иванов', 'неБосс', 10, 0)

is_obj_exist(worker1, 'get_full_name')
is_obj_exist(worker1, 'get_total_income')
print()
is_obj_exist(worker2, 'get_full_name')
is_obj_exist(worker2, 'get_total_income')
print()
is_obj_exist(worker3, 'get_full_name')
is_obj_exist(worker3, 'get_total_income')
