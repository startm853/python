from random import randrange

start_list = [randrange(30) for el in range(30)]
# start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in start_list if start_list.count(el) == 1]

print(start_list)
print(new_list)
