"""
Задача 49.Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет самую большую
площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
которая среди списка орбит планет найдет ту, по которой вращается самая
далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей
звезды таких планет нет, зато искусственные спутники были были запущены
на круговые орбиты. Результатом функции должен быть кортеж, содержащий
длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее эллипса.
Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса.
При решении задачи используйте списочные выражения.
Подсказка: проще всего будет найти эллипс в два шага:
сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
"""
from math import pi


def find_farthest_orbit(list_of_orbits: list) -> tuple:
    squares_iterable = map(lambda el: pi * el[0] * el[1] if el[0] != el[1] else None, list_of_orbits)
    squares_list = list(squares_iterable)
    max_square = max(filter(lambda el: el is not None, squares_list))
    index_of_max_square = squares_list.index(max_square)
    return list_of_orbits[index_of_max_square]


def main() -> None:
    orbits = [(6, 6), (1, 3), (2.5, 10), (7, 2), (4, 3)]
    print(*find_farthest_orbit(orbits))


if __name__ == '__main__':
    main()

"""
решение от Андрея Крылова 
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

orbits_square = lambda orbits: list(int(3.14 * i[0] * i[1]) for i in orbits if i[0] !=  i[1])
print(*orbits_square(orbits))
find_farthest_orbit = lambda array: list(i for i in orbits if int(3.14 * i[0] * i[1]) == min(orbits_square(orbits)))      
print(*find_farthest_orbit(orbits))
"""

"""
решение от Владимира

import os
import json


def del_conact(contacts: list) -> dict:
    print('Какой контакт желаете удалить?')
    found = find_contact(contacts)
    print(found)
    if found:
        show_on_screen(found)
        value = input('Подтвердите операцию удаления: Да/Нет\n>>>')
        if value.lower() == 'да':
            contacts.remove(found[0])
            print('Удаление завершено.')
            return {}
        elif value.lower() == 'нет':
            print('Команда удаления отменена.')
            return {}
        else:
            print('Введена неверна команда.')
            return {}
    else:
        print('Никого не нашли ;(')
        return {}


def save_change_contact(contacts: list) -> dict:
    found = find_contact(contacts)
    if found:
        show_on_screen(found)
        # print(found)
        value = input('Что желаете изменить?\n>>>').lower()
        if value == 'имя':
            found[0]['first_name'] = input('Введите новое имя:\n>>> ').upper()
        elif value == 'фамилию':
            found[0]['second_name'] = input('Введите фамилию:\n>>> ').upper()
        elif value == 'номер':
            found[0]['contacts'] = input('Введите новый номер телефона:\n>>>')
    else:
        print('Никого не нашли ;(')
        return {}


def find_contact(contacts: list) -> dict:
    first_name = input('Введите имя:\n>>> ').upper()
    second_name = input('Введите фамилию:\n>>> ').upper()
    found = list(filter(lambda el: first_name in el['first_name'] and second_name in el['second_name'], contacts))
    if found:
        show_on_screen(found)
        return found
    else:
        print('Никого не нашли ;(')
        return {}


def file_path(file_name='contact_list'):
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')


def load_from_file():
    path = file_path()
    if os.stat(path).st_size:

        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        return data
    else:
        return []


def save_to_file(contact: list) -> None:
    path = file_path()

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(contact, file, ensure_ascii=False)


def show_on_screen(contacts: list) -> None:
    decode_keys = dict(
        first_name='Имя:',
        second_name='Фамилия:',
        contacts='Телефон:'
    )
    pretty_text = str()
    for num, elem in enumerate(contacts, 1):
        pretty_text += f'Контакт №{num}:\n'
        pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
        pretty_text += '\n________\n'
    print(pretty_text)


def new_contact(contacts: list) -> None:
    # Контактной информации может быть больше чем только телефон
    contacts.append(
        dict(
            first_name=input('Введите имя контакта:\n>>> ').upper(),
            second_name=input('Введите фамилию контакта:\n>>> ').upper(),
            contacts=input('Введите номер телефона:\n>>> ').upper()
        )
    )


def menu():
    commands = [
        'Показать все контакты',
        'Найти контакт',
        'Создать контакт',
        'Изменить контакт',
        'Удаление контакта'
    ]
    print('Укажите номер команды:')
    print('\n'.join(f'{n}. {v}' for n, v in enumerate(commands, 1)))
    choice = input('>>> ')

    try:
        choice = int(choice)
        if choice < 0 or len(commands) < choice:
            raise Exception('Такой команды пока нет ;(')
        choice -= 1
    except ValueError as ex:
        print('Я вас не понял, повторите...')
        menu()
    except Exception as ex:
        print(ex)
        menu()
    else:
        return choice


# def tests():
#     contact = dict(
#         first_name='Иван',
#         second_name='Иванов',
#         contacts='123'
#     )
#     contact2 = dict(
#         first_name='Петр',
#         second_name='Петров',
#         contacts='123'
#     )
#     contact3 = dict(
#         first_name='Петр',
#         second_name='Иванов',
#         contacts='123'
#     )
#     contact4 = dict(
#         first_name='Иван',
#         second_name='Петров',
#         contacts='123'
#     )
#     contacts = [contact, contact2, contact3, contact4]
#     return contacts


def main() -> None:
    print('Программа запущена...')
    data = load_from_file()

    command = menu()
    if command == 0:
        show_on_screen(data)
    elif command == 1:
        find_contact(data)
    elif command == 2:
        # tests()
        new_contact(data)
    elif command == 3:
        save_change_contact(data)
    elif command == 4:
        del_conact(data)
    save_to_file(data)
    print('Конец программы!')


if __name__ == '__main__':
    main()
"""