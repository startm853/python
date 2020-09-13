# Words
# Test: Ввожу несколько слов и некоторые из них должны быть оооооооооооооооочень длинными

words = input('Введите что-нибудь\n').split()

for word in enumerate(words):
    print(f'{word[0] + 1}: {word[1]:.10}')
