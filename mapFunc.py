numbers = [5, 3, 4, 7, 8]

# получить список квадратов чисел
# первый параметр - что будет делать наша функция?
# lambda x: x**2 - возводить число x в степень 2
# второй параметр - это последовательность numbers

print(list(map(lambda x: x**2, numbers)))
# привести числа к строке
# функцией выступает str(x) - приводит числовые значения
# к строке и выводит в '' скобках
print(list(map(lambda x: str(x), numbers)))
