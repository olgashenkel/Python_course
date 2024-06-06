# Винни Пух
#
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу.
#
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
#
# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки.
# В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести:
# Количество фраз должно быть больше одной!
#
##############
# Пример
#
# На входе:
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:
# Парам пам-пам
###############################################

stroka = 'пара-ра-рам'


def rhythm(stroka):
    number_spaces = stroka.count(" ")
    stroka = stroka.split()
    array = []
    for item in stroka:
        result = 0
        for i in item:
            if i in 'аеёиоуыэюя':
                result += 1
        array.append(result)
    return len(array) == array.count(array[0])


if rhythm(stroka) and stroka.count(" ") >= 1:
    print('Парам пам-пам')
elif rhythm(stroka) and stroka.count(" ") < 1:
    print('Количество фраз должно быть больше одной!')
else:
    print('Пам парам')


# Решение с сайта:
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()
# if len(phrases) < 2:
#  print('Количество фраз должно быть больше одной!')
# else:
#  countVowels = []
#
#  for i in phrases:
#   countVowels.append(len([x for x in i if x.lower() in vowels]))
#
#  if countVowels.count(countVowels[0]) == len(countVowels):
#   print('Парам пам-пам')
#  else:
#   print('Пам парам')