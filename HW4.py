"""
Задача 4. Петя, Катя, и Сережа делают
из бумаги журавликов. Вместе они
сделали S журавликов. Сколько журавликов
сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала
в два раза больше журавликов, чем Петя
и Сережа вместе?
"""

s = int(input('Введите количество журавликов: '))
if s % 6 == 0:
    serg = int(s / 6)
    petr = serg
    kate = 2 * (serg + petr)
    print('Петя сделал', petr, 'журавликов, Катя',
          kate, 'журавликов, Сережа', serg, 'журавликов')
else:
    print('Введите число журавликов, кратное 6')