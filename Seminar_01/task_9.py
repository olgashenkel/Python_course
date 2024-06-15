a = 2
while a > 0:
    print(a)
    if a == 3:
        break
    a -= 1
else:
    print("Завершение цикла не по break")

my_str = "jhgfgkfk"
for el in my_str:
    print(el, end=" ")


i = 0
while i < len(my_str):
    print(my_str[i], end=" ")
    i += 1