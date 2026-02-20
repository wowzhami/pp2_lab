x  = pow(2, 3) 
print(x) # 8 

import math
x = math.sqrt(64)
print(x) #8


import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

import math
x = math.pi
print(x) #3.141592653589793




#random 
import random

# Генерируем число от 0.0 до 1.0
coin = random.random()
if coin < 0.5:
    print("Орел 🦅")
else:
    print("Решка 🪙")

print(f"(Выпало число: {coin:.2f})")

#число в диапазоне
import random
print(random.randint(1, 6))  # Имитация броска кубика


#один случайный элемент из списка, строки или кортежа
fruits = ["яблоко", "банан", "вишня"]
print(random.choice(fruits))  # Выберет что-то одно




#Меняет порядок элементов в самом списке. 
cards = ["Туз", "Король", "Дама"]
random.shuffle(cards)
print(cards)  # Порядок изменился
