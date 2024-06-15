# поменять местами первый и последний элемент списка

list_1 = [5, 10, 653, 784, 2, 0]

last = list_1.pop()
first = list_1.pop(0)

list_1.insert(0, last)
list_1.append(first)

print(list_1)

my_dict = {1:1, 2:2}

a = 1
a = 123
a[2] = 5 # НЕЛЬЗЯ менять, так как число неизменяемый тип
