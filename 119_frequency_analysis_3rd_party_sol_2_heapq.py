# Date: 07.08.2022
# Lessons from pytontutor.ru
# Заняття 11. Словники
# Завдання "Частотний аналіз"

# Умова
# Даний текст: у першому рядку записано кількість рядків у тексті, а потім самі рядки. Виведіть всі
# слова, що зустрічаються в тексті, по одному на кожен рядок. Слова повинні бути відсортовані за
# зменшенням їх кількості появи в тексті, а при однаковій частоті появи - в лексикографічному
# порядку.

import heapq
from collections import Counter as C
s = str()
for _ in range(int(input())):
    s += input()
    s += " "
s = s.split()
c = C(s)
heap = []
for k, v in c.items():
    heapq.heappush(heap, (-v, k))
res = ""
while heap:
    res += heap[0][1] + " "
    heapq.heappop(heap)
print(res)
