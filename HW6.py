"""
Задача 6. Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет
с номером. Счастливым билетом называют такой билет
с шестизначным номером, где сумма первых трех цифр
равна сумме трех последних. Т.е. билет с номером
385916 является счастливым

функция list преобразовывает  строку с числом в
список строк с цифрами; функция map преобразовывает
каждый элемент полученного списка строк с цифрами
в список целых чисел функция sum суммирует числа
"""

number = input('Введите шестизначный номер билета: ')
if number.isdigit():
    print(' ')
else:
    print('Ошибка, вы ввели неверный номер')

result1 = (number[:-3:])
result2 = (number[3::])
list_string1 = list(result1)
list_string2 = list(result2)
list_num1 = map(int, list_string1)
list_num2 = map(int, list_string2)
sum1 = sum(list_num1)
sum2 = sum(list_num2)
if sum1 == sum2:
    print('Поздравляем, у Вас счастливый билет! Cумма '
          'первых трёх цифр и трёх последних равна', sum1)
else:
    print('К сожалению, Вам не достался счастливый билет, '
          'поскольку сумма первых трёх цифр, равная', sum1,
          'не равна сумме трёх последних цифр равной', sum2)
