# Switch Elements
# Test: 1 , привет, 3,несколько слов, False, 6, True, восьмой, 9, последний

data = input('Введите список элементов через запятую\n')
data = data.replace(', ', ',').replace(' ,', ',').split(',')
data2 = data.copy()

for i in range(0, len(data), 2):
    tmp = data[i]
    data.remove(data[i])
    data.insert(i + 1, tmp)
print(data)

# Альтернативная реализация
for i in range(1, len(data2), 2):
    tmp = data2[i - 1]
    data2[i - 1] = data2[i]
    data2[i] = tmp
print(data2)
