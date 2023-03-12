# Напишите программу угадай число для нескольких пользователей

import random

number = random.randint(1, 100)
# print(number)  # вывод числа на экран для тестирования программы

user_number = None
count = 0
# задаем количество уровней через словарь, где 1 - уровень,
# 10 - ключ - то есть количество попыток
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности от 1 до 3: '))
# в [] скобках вводится ключ: либо число либо переменная
max_count = levels[level]  # вводим ограничение на количество попыток

# шаг 1 определяем количество пользоваетелей
user_count = int(input('Введите количество игроков: '))
users = []  # создаем пустой список
for i in range(user_count):  # проходим по всему циклу для каждого пользователя
    # f - функция красивого вывода на консоль
    user_name = input(f'Введите имя пользователя {i}:  ')
    users.append(user_name)  # добавляем имя пользователя в список users

# шаг 3. Вводим новые переменные и задаем условия выхода из цикла
# для нескольких пользователей
is_winner = False
winner_name = None

while number != user_number:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли :(')
        break
    # шаг 2. Определяем очередность хода пользователей
    # т.к. пользователей много, то будем проходить по циклу for
    for user in users:
        print(f'Ход пользователя {user}')
        print(f'Попытка № {count}')

        user_number = int(input('Введите число: '))
        # после ввода числа пользователем проверяем его
        if user_number == number:
            is_winner = True
            winner_name = user
            break  # ставим условие выхода из цикла
        elif number < user_number:
            print('Введенное число больше загаданного')
        else:
            print('Введенное число меньше загаданного')

else:
    # c {user} вывод тоже работает корректно
    print(f'Победитель {winner_name}, поздравляем!')
