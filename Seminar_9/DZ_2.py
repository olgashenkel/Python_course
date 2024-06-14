# Максимальная households

# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения
# переменной population и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.
###############################################

from pandas import read_csv

data = read_csv('california_housing_train.csv')

max_households_in_min_population = data[data['population'] == data['population'].min()]['households'].max()

print(max_households_in_min_population)



# Решение с сайта:
# import pandas as pd
#
# df = pd.read_csv('california_housing_train.csv')
# # Найти минимальное значение 'population'
# min_population = df['population'].min()
#
# # Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
# max_households_in_min_population = df[df['population'] == min_population]['households'].max()