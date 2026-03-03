import re

text = "В 2023 году было 12 месяцев, а в 2024 будет столько же."
# Ищем все последовательности цифр (\d+)
result = re.findall(r"\d+", text)
print(result) 
# Вывод: ['2023', '12', '2024']


text = "Кот сидит на крыше, а другой кот под крышей."
match = re.search(r"кот", text, re.IGNORECASE) # Игнорируем регистр
if match:
    print(f"Найдено: {match.group()}") # Текст совпадения - Кот
    print(f"Начало: {match.start()}")   # Индекс начала - 0
else:
    print("Ничего не найдено")



text = "Яблоки,груши;апельсины сливы"
# Разделяем по запятой, точке с запятой или пробелу
result = re.split(r"[,; ]", text)
print(result)
# Вывод: ['Яблоки', 'груши', 'апельсины', 'сливы']



text = "Секретный код: 123-456. Еще один код: 000-111."
# Заменяем все цифры на знак '*'
result = re.sub(r"\d", "*", text)
print(result)
# Вывод: Секретный код: ***-***. Еще один код: ***-***.



#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) #    .* anything
if x:
  print("YES! We have a match!") # print this
else:
  print("No match") 



#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) #['ai', 'ai'] else [] 



txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 
#The first white-space character is located in position: 3



#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#['The', 'rain', 'in', 'Spain']

#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)  #['The', 'rain in Spain']




#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#The9rain9in9Spain



#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
#The9rain9in Spain 