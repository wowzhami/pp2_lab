names = ["Анна", "Борис", "Виктор"]
scores = [85, 92, 78]
# Склеиваем два списка
combined = zip(names, scores)
# Превращаем результат в список, чтобы его увидеть
print(list(combined))
# Вывод: [('Анна', 85), ('Борис', 92), ('Виктор', 78)]



shopping_list = ["Яблоки", "Молоко", "Хлеб"]
# enumerate() возвращает пары (индекс, значение)
for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")
# Вывод:
# 1. Яблоки
# 2. Молоко
# 3. Хлеб