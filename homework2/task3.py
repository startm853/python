# Get Month

dict_seasons = {
    'winter': ['1', '2', '12', 'jan', 'feb', 'dec'],
    'spring': ['3', '4', '5', 'mar', 'apr', 'may'],
    'summer': ['6', '7', '8', 'june', 'july', 'aug'],
    'autumn': ['9', '10', '11', 'sept', 'oct', 'nov'],
}

month = input('Введите месяц:\n').lower()

for seasons in dict_seasons.items():
    if month in seasons[1]:
        print(seasons[0])
        break
