# Rating

rating = [7, 5, 3, 3, 2]

new_value = int(input('Введите новое значение\n'))

if new_value <= rating[-1]:
    rating.append(new_value)
else:
    for r in enumerate(rating):
        if new_value > r[1]:
            rating.insert(r[0], str(new_value))
            break

print(rating)
