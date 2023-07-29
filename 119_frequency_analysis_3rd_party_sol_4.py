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
d = {}

for i in range(n):
    line = input().split()
    
    for j in line:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
            
m = {}      

for key, value in d.items():
    if value in m:
        m[value].append(key)
    else:
        m[value] = [key]

for i in sorted(m.items(), reverse=True):
    print('\n'.join(sorted(i[1])))
