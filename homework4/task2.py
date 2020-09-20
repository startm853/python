from random import randrange

start_list = [randrange(300) for el in range(10)]
new_list = [el for i, el in enumerate(start_list[1:]) if el > start_list[i]]
print(start_list)
print(new_list)
