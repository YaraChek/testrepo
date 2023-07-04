#!/usr/bin/python3

# Завдання на програмування: кодування Хаффмана
# https://stepik.org/lesson/13239/step/5?unit=3425

# За цим непустим рядком s довжини не більше 10⁴, що складається з малих літер латинського алфавіту,
# побудуйте оптимальний безпрефіксний код. У першому рядку виведіть кількість різних букв k,
# зустрічаються в рядку, і розмір закодованого рядка, що вийшов. У наступних k рядках запишіть
# коди букв у форматі "letter: code". В останньому рядку виведіть закодований рядок.

# Sample Input 1:
# a

# Sample Output 1:
# 1 1
# a: 0
# 0

# ------------------------------
# Sample Input 2:
# abacabad

# Sample Output 2:
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111

# input: Passed test #9:
# 'accepted'

# output: Passed test #9:
# 10100000110011101110 - мій кодує інакше, але stepik рішення приймає

import heapq
from collections import Counter

s = input()
encrypt_dict = dict.fromkeys(list(set(s)), '')  # словник для кодування/декодування
character_queue = []  # список черги з пріоритетами
code = []  # список с нулями й одиницями

# визначаємо як часто символ входить у рядок
[character_queue.append((volume, key)) for key, volume in Counter(s).items()]
character_queue.sort()

# перетворюємо список на heap, щоб зручно було виймати 2 мінімальні елементи,
# для того, щоб скласти їх пріоритети та додати в купу (heap) новый елемент із сумою їх пріоритетів
heapq.heapify(character_queue)

while len(character_queue) > 1:
    temp1 = heapq.heappop(character_queue)
    code.append(('0', temp1[1]))
    temp2 = heapq.heappop(character_queue)
    code.append(('1', temp2[1]))
    heapq.heappush(character_queue, (temp1[0] + temp2[0], temp1[1] + temp2[1]))

temp1 = heapq.heappop(character_queue)
code.append(('', temp1[1]))

for char in encrypt_dict:
    for i in range(len(code)):
        if char in code[i][1]:
            # 0 чи 1 додаємо в початок кодуючого рядка
            # для того, щоб код виходив беспрефіксным
            encrypt_dict[char] = code[i][0] + encrypt_dict[char]
    
encrypt_string = ''
if len(set(s)) < 2:
    encrypt_dict[s[0]] = '0'

for char in s:
    encrypt_string += encrypt_dict[char]

print(len(encrypt_dict), len(encrypt_string))

for k, v in encrypt_dict.items():
    print(f'{k}: {v}')
print(encrypt_string)
