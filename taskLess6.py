"""
1: Создайте функцию, принимающую на вход имя,
возраст и город проживания человека. Функция
должна возвращать строку вида «Денис,
21 год(а), проживает в городе Москва»
"""


def person_info(name, age, city):
    result = f'{name}, {age} год(а) проживает в городе {city}'
    return result


print(person_info('Денис', 21, 'Ижевск'))

# вторая задача
# напишите функцию, принимающую на вход
# 3 числа и возвращающую наибольшее из них.


def get_max(a, b, c):
    result = max([a, b, c])
    return result


result = get_max(1, 5, 3)
print(result)

print(get_max(7, 1, 6))
