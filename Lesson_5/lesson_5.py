# -*- coding: utf-8 -*-
"""Lesson_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T2rcUmA1GvGiMvytTQgubR8bOTiHBG6N
"""

import pandas as pd

# @title
# читаем
df = pd.read_csv('sample_data/california_housing_train.csv', sep=';')
# добавили аргумент sep - разделитель (по умолчанию разделитель точка с запятой,
# если так и должно быть, аргумент sep можно не выставлять,
# вместо ; можно поставить другой разделитель)

df.head(n=10)
# с помощью функции head - считываем данные таблицы
# n = 10 -> выводится 10 строк таблицы (отсчет начинается с 0. Можно задать больше или меньше значений строк)

df.tail(n=5)
# функция tail - выводит последние элементы (в данном слачае n = 5 (т.е. 5 элементов))

df.shape
# функция shape - позволяет посмотреть общий размер таблицы (количество строк, столбцов)


df.isnull()
# функция isnull - позволяет просмотреть нулевые (пустые) значения

df.isnull().sum()
# функция isnull - позволяет просмотреть нулевые (пустые) значения
# дополнительная функция sum - суммирует все ячейки

df.dtypes
# функция dtypes - позволяет увидеть тип данных столбца

df.columns
# функция columns - позволяет увидеть все столбцы. В результате выходит список названий всех столбцов таблицы

"""---

# **Выборка данных**
"""

df['latitude']
# вывод данных столбца 'latitude'

df[['latitude', 'population']]
# вывод данных нескольких столбцов

"""**Задание:** Необходимо вывести столбец **total_rooms**, у которого медианный возраст
здания(**housing_median_age**) меньше **20**.

"""

df[df['housing_median_age'] < 20]

df[df['housing_median_age'] < 20]['total_rooms']

"""**&** - выполнение одновременно **всех** условий

**|** - выполнение **хотя бы одного** из условия
"""

df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)]['total_rooms']

df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)][['total_rooms', 'housing_median_age']]
# [[]] - список в списке

"""---

# **Простая статистика**
"""

print(df['population'].max())
# максимальное значение определенного столбца

print(df['population'].min())
# минимальное значение определенного столбца

print(df['population'].mean())
# среднее значение определенного столбца

print(df['population'].sum())
# суммарное значение определенного столбца

print(df['population'].median())
# медианное (среднее) значение определенного столбца

print(df[['population', 'total_rooms']].median())
# медианное (среднее) значение определенного столбца
# [[]] - список в списке

df.describe()
# функция describe - Получить общую картину можно простой командой describe

"""**count** - Общее кол-во не пустых строк <br>
**mean** - среднее значение в столбце <br>
**std** - стандартное отклонение от среднего значения <br>
**min** - минимальное значение <br>
**max** - максимальное значение <br>
Числа **25%, 50%, 75%** - перцентили <br>
**Перцентиль** - это показатель, используемый в статистике, показывающий значение, ниже которого падает определенный процент
наблюдений в группе наблюдений

---

# **Изображаем статистические отношения**

### **Scatterplot (Точечный график)**
Математическая диаграмма, изображающая значения двух переменных в виде
точек на декартовой плоскости. Библиотека **seaborn** без труда принимает **pandas
DataFrame(таблицу)**. Чтобы изобразить отношения между двумя столбцами
достаточно указать, какой столбец отобразить по оси **x**, а какой по оси **y**.<br>
Для того чтобы начать работу с библиотекой seaborn, ее необходимо импортировать
к себе в программу:<br>
**import seaborn as sns**
"""

import seaborn as sns
# pip install seaborn - установка модуля seaborn
"""Изображение точек долготы по отношению к широте:"""

sns.scatterplot(data=df, x="longitude", y="latitude")

"""Отношение, чем выше кол-во семей, тем выше кол-во людей и соответственно комнат.

Помимо двумерных отношений, мы можем добавить "дополнительное измерение" с
помощью цвета. В данном случае опять же достаточно очевидное отношение, чем
выше кол-во семей, тем выше кол-во людей и соответственно комнат.
"""

sns.scatterplot(data=df, x="households", y="population", hue="total_rooms")

"""Помимо обозначения дополнительного измерения цветом мы можем использовать
size.
"""

sns.scatterplot(data=df, x="households", y="population", hue="total_rooms", size=10)

"""Мы можем визуализировать сразу несколько отношений, используя класс PairGrid
внутри seaborn. PairGrid принимает как аргумент pandas DataFrame и
визуализирует все возможные отношения между ними, в соответствии с
выбранным типом графика.
"""

cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
g = sns.PairGrid(df[cols])
g.map(sns.scatterplot)

"""# **Линейные графики**

Хорошо подойдут, если есть временная или какая-либо иная последовательность и
значения, которые могут меняться в зависимости от нее. Для генерации линейных
графиков в **seaborn** используется **relplot** функцию. Она также принимает
**DataFrame, x, y** - столбцы.<br>
Для визуализации выбирается тип **line**:
"""

sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)

"""Можно видеть, что в определенных местах долготы цена за дома резко
подскакивает.

Попробуем визуализировать longitude по отношения к median_house_value и поймем
в чем же дело, почему цена так резко подскакивает.
"""

sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)

"""Можно видеть, что в определенных местах широты цена за дома также очень
высока.

Используя точечный график можно визуализировать эти отношения с большей
четкостью. Скорее всего резкий рост цен связан с близостью к ценному объекту,
повышающему качество жизни, скорее всего побережью океана или реки.
"""

sns.scatterplot(data=df, x="latitude", y="longitude", hue="median_house_value")

"""---

# **Гистограмма**

Способ представления табличных данных в графическом виде — в виде столбчатой
диаграммы. По оси x обычно указывают значение, а по оси y - встречаемость(кол-во
таких значений в выборке)
"""

sns.histplot(data=df, x="median_income")

"""Можно видеть что у большинства семей доход находится между значениями 2 и 6. И
только очень небольшое количество людей обладают доходом > 10.

Изобразим гистограмму по housing_median_age.
"""

sns.histplot(data=df, x='housing_median_age')

"""Распределение по возрасту более равномерное. Большую часть жителей
составляют люди в возрасте от 20 до 40 лет. Но и молодежи не мало. Также очень
много пожилых людей > 50 лет медианный возраст.

Давайте посмотрим медианный доход у пожилых жителей.
"""

sns.histplot(data=df[df['housing_median_age'] > 50], x="median_income")

"""Большого отличия от популяции в целом не наблюдается. Скорее всего это местные
жители.

Давайте разобьем возрастные группы на 3 категории те кто моложе 20 лет, от 20 до
50 и от 50, чтобы посмотреть влияет ли это на доход.
"""

df.loc[df['housing_median_age'] <= 20, 'housing_median_age']

df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'

"""Что в этом случае происходит внутри таблицы? Добавился новый столбец
**age_group**, в котором будет указана соответствующая категория.
"""

df.columns

"""Применим group_by, чтобы получить среднее значение."""

df.head()

df.groupby('age_group')['median_income'].mean().plot(kind='bar')

"""**Seaborn** так же позволяет нам смотреть распределение по многим параметрам.
Давайте поделим группы по доходам на 2. Те у кого медианный доход выше 6 и те у
кого меньше. Изобразим дополнительное измерение с помощью оттенка в виде
возрастных групп и групп по доходам.
"""

df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'

df.columns

df.head()

sns.displot(df, x="median_house_value", hue="income_group")
