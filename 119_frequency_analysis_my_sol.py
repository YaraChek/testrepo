# Date: 07.08.2022
# Lessons from pytontutor.ru
# Заняття 11. Словники
# Завдання "Частотний аналіз"

# Умова
# Даний текст: у першому рядку записано кількість рядків у тексті, а потім самі рядки. Виведіть всі
# слова, що зустрічаються в тексті, по одному на кожен рядок. Слова повинні бути відсортовані за
# зменшенням їх кількості появи в тексті, а при однаковій частоті появи - в лексикографічному
# порядку.

text = []
numbers_list = []
for i in range(int(input())):
    text.extend(input().split())
words_list = list(set(text))
for i in words_list:
    numbers_list.append(text.count(i))

sorted_list = dict(sorted([(words_list[i], numbers_list[i]) for i in range(len(words_list))]))
for i in range(max(numbers_list), 0, -1):
    for k, v in sorted_list.items():
        if v == i: print(k)