numbers = [1, 2, 3, 4]
# Функция map(что сделать, с чем сделать)
squared = map(lambda x: x**2, numbers)
print(list(squared)) 
# Вывод: [1, 4, 9, 16]


numbers = [1, 2, 3, 4, 5, 6]
# Оставляем только те x, которые делятся на 2 без остатка
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))
# Вывод: [2, 4, 6]