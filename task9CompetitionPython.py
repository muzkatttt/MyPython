"""
Пользователь вводит количество участников
соревнований по python. Далее пользователь
вводит участников и их места с конца в зависимости
от количества участников
1. Вывести именя участников по алфавиту
2. Получить 3-х победителей  и поздравить их
3. Вывести на экран: Победители:    Поздравляем!
"""

print('Соревнования по Python')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место '.format(i))
    members.append(name)
    i -= 1

# кто участвовал в соревновании (по алфавиту)
print('В соревновании участвовали: ', sorted(members))

# Мы записали людей с конца списка
members.reverse()

# необходимо перечислить первые 3 места
result = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)
