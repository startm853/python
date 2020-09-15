# Телефон, email, дата виладируются регулярками, поэтому в этой задаче ничего не стал проверять

def user_data(**kwargs):
    return kwargs


user = user_data(first_name=input('Введите имя:\n'), second_name=input('Введите фамилию:\n'),
                 birthday=input('Введите день рождения:\n'), city=input('Введите город:\n'),
                 email=input('Введите email:\n'), phone=input('Введите телефон:\n'))
print(user)
