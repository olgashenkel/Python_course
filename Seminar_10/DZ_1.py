# Промежуточная аттестация
#############################
# Задача 44:
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
######################
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
########################

import random

import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# 1-ый способ:
data['robot'] = [1 if lst_1 == 'robot' else 0 for lst_1 in data['whoAmI']]
data['human'] = [1 if lst_2 == 'human' else 0 for lst_2 in data['whoAmI']]

print(f'\n1-ый способ:\n {data.head(n=5)}\n')


# 2-ой способ:
data['robot'] = (data['whoAmI'] == 'robot').astype(int)
data['human'] = (data['whoAmI'] == 'human').astype(int)

print(f'2-ой способ:\n {data.head(n=5)}')