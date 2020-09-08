# Workout

a = float(input('Укажите результат спортсмена A:\n'))
b = float(input('Укажите результат спортсмена B:\n'))

days = 1
while a < b:
    a = a * 1.1
    days += 1

print(days)
