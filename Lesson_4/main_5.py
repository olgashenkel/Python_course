# Функция filter
#####################
# 💡 Функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами, для которых
# функция вернула True.

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x%10 == 5, data))
print(res)


lst_1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, lst_1)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)