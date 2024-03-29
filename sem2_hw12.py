"""
Задача 12: Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница. Петя
помогает Кате по математике. Он задумывает
два натуральных числа X и Y (X,Y≤1000), а
Катя должна их отгадать. Для этого Петя
делает две подсказки. Он называет сумму
этих чисел S и их  произведение P.
Помогите Кате отгадать задуманные Петей числа
"""

def guess_numbers():
    sum = int(input('Введите сумму чисел: \n'))
    multiplication = int(input('Введите произведение чисел: \n'))
    x = 0
    y = 0

    for i in range(1, min(sum, multiplication) + 1):
        for j in range(1, min(sum, multiplication) + 1):
            if i + j == sum and i * j == multiplication:
                x = i
                y = j
    print(f'Первое загаданное число = {x}, второе = {y}')


guess_numbers()
