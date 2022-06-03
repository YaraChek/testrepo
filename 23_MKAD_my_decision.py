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

a = int(input('Enter'))
b = int(input())
print((a * b) % 109)