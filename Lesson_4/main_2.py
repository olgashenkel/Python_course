# Задача для самостоятельного решения
# В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]
# Решение:

# lst_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# lst_2 = []
# for i in lst_1:
#     if i % 2 == 0:
#         lst_2.append((i, i ** 2))
#
# print(lst_2)

########################
# Решение с помощью lambda-функции:

# def select(f, col):
#     return [f(x) for x in col]
#
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# lst_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, lst_1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

########################
# Решение с помощью map():

def where(f, col):
    return [x for x in col if f(x)]


lst_1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, lst_1)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)