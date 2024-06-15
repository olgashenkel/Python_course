'''
Ближайший элемент в массиве
Требуется найти в массиве list_1 самый близкий по значению элемент
к заданному числу k и вывести его.
Считать, что такой элемент может быть только один.
Если значение k совпадает с этим элементом - выведите его.

Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5

'''

list_1 = [2, 4, 1, 9, 6, 2, 3, 2, 5, 11, 15, 25]
k = 10
count = list_1[0]

for i in range(1, len(list_1)):
    if abs(k - list_1[i]) <= abs(k - count):
        count = list_1[i]

print(count)

print(k - list_1[i])
"""
Решение с сайта:

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
"""

