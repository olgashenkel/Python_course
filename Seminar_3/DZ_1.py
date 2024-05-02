'''
Встречаемость элемента в массиве
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.

Пример:
list_1 = [1, 2, 3, 4, 5]
k = 3
# 1
'''

list_1 = [1, 2, 3, 4, 5, 3, 3, 4, 5]
k = 7

print(f"{list_1.count(k)}")


"""
Решение с сайта:

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)

"""