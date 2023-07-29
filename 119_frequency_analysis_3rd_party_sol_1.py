# Date: 07.08.2022
# Lessons from pytontutor.ru
# Заняття 11. Словники
# Завдання "Частотний аналіз"

# Умова
# Даний текст: у першому рядку записано кількість рядків у тексті, а потім самі рядки. Виведіть всі
# слова, що зустрічаються в тексті, по одному на кожен рядок. Слова повинні бути відсортовані за
# зменшенням їх кількості появи в тексті, а при однаковій частоті появи - в лексикографічному
# порядку.

n = int(input())
a = dict()
for i in range(n):
    s = list(map(str, input().split()))
    for j in s:
        try:
            a[j] += 1
        except KeyError:
            a[j] = 0
b = sorted(a.values(), reverse = 'True')
c = sorted(a.keys())
for i in b:
    for j in c:
        if i == a[j]:
            print(j)
            a[j] = -1
