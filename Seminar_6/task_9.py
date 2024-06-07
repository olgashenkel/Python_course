"""
Задание 34
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.

Решите через dc.
"""


def func(names, salaries, awards):
    return {name: salary * float(award.rstrip('%')) / 100 for name, salary, award in zip(names, salaries, awards)}


names = ['Борис', 'Семен', 'Петр', 'Сергей']
salaries = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85%']

print(func(names, salaries, awards))

# метод .rstrip() - убирает необходимый символ