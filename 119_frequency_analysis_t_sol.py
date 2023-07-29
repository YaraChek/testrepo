# Date: 07.08.2022
# Lessons from pytontutor.ru
# Заняття 11. Словники
# Завдання "Частотний аналіз"

# Умова
# Даний текст: у першому рядку записано кількість рядків у тексті, а потім самі рядки. Виведіть всі
# слова, що зустрічаються в тексті, по одному на кожен рядок. Слова повинні бути відсортовані за
# зменшенням їх кількості появи в тексті, а при однаковій частоті появи - в лексикографічному
# порядку.

from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))
