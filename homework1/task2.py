# TimeConverter

ticks = 60
minutes = 0
hours = 0

while True:
    seconds = int(input('Введите количество секунд\n'))
    if seconds >= 0:
        if seconds >= ticks:
            minutes = seconds // ticks
            seconds = seconds % ticks
            if minutes >= ticks:
                hours = minutes // ticks
                minutes = minutes % ticks
        print(f'{hours:02}:{minutes:02}:{seconds:02}')
        break
    else:
        print('Хорошая попытка')
