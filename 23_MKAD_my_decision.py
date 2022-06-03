# Дата: 28.05.2022
# Файл “MKAD”
# Уроки с pythontutor.ru
# Задача “МКАД”

# Условие
# Длина Московской кольцевой автомобильной дороги - 109 километров.
# Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v к/ч.
# На какой отметке он остановится через t часов?

# Программа получает на вход значение v и t.
# Если v>0, то Вася движется в положительном направлении по МКАД,
# если же значение v<0, то в отрицательном.

# Программа должна вывести целое число от 0 до 108 - номер отметки,
# на которой остановится Вася.

road = 109
v = int(input("v = "))
t = int(input("t = "))
s = abs(v * t)

b = s - (road - 1)
boo1 = b < 0

while boo1 == False:
    s -= road
    b = s - (road - 1)
    boo1 = b < 0
    if boo1 == True:
        break

grade = s

if v < 0:
    grade = road - s
if grade == 109:
    grade = 0

print(grade)