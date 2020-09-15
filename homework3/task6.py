def int_func(text):
    """
    Если первый символ не буквенный, то title() переводит следующий буквенный символ в вверхний регистр
    """
    return text.title()


def int_func_2(text):
    """
    Если первый символ не буквенный, то строка отсается в первоначальном виде
    """
    data = text.split()
    result = ''
    for i in data:
        result = result + ' ' if result != '' else result
        result = result + i[0].upper() + i[1:]
    return result


# Test: пыфпфы fgsgas дарвеыgsag gdgsпыф2 44gdsgав3 афППпуфыFSfdg
while True:
    input_text = input('Введите текст:\n')
    if not input_text.islower():
        print('Вводимые символы должны быть в нижнем регистре\n')
    else:
        print(int_func(input_text))
        print(int_func_2(input_text))
    again = input(f"{'-' * 50}\n[Q] - выход\n[Enter] - попробовать еще раз\n")
    if again.lower() == 'q':
        break
