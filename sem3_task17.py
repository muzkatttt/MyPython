"""
Задача 17. Дан список чисел. Определите,
сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
"""

l = [1, 1, 2, 0, -1, 3, 4, 4]

def how_many_dif_elements(list):
    list = set(list)
    print(l)
    print(f'There are - {len(list)} different elements in given list')

how_many_dif_elements(l)
