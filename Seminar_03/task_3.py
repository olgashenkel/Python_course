'''
Задача №21.
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
'''

list_dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
               {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
set_1 = set()
for dict_1 in list_dict_1: # dict_1 - итератор
    for value in dict_1.values():  # values - отсекает дубли
        set_1.add(value)
print(set_1)

print(set_1)
# сэт компрехэншен - множественное включение:
print({dict_1[item] for dict_1 in list_dict_1 for item in dict_1})