"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6

0 1 1 2 3 5 8
"""

a = 5
fibo_p, fibo_n = 0, 1
position = 2
while fibo_n < a:
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
    position += 1
if fibo_n == a:
    print(position)
else:
    print(-1)


# Рекурсия:
def func(a, fibo_p=0, fibo_n=1, position=2):
    if fibo_n == a:
        return position
    elif fibo_n < a:
        return func(a, fibo_n, fibo_p + fibo_n, position + 1)
    else:
        return "-1"


print(func(5))
