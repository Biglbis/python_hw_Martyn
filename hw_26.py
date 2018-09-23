"""
Создайте список из 11 случайных целых чисел из отрезка [-1;1].
Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент.
Однако, если два каких-то элемента встречаются одинаковое количество раз, то вернуть None,
а не самый часто встречающийся элемент, даже если дублирующиеся элементы не максимальны!
     def calc_frequency(lst): # returns the most frequent number or None
		pass
	Например:
		для [1, 1, 1, -1, -1, 1, 1, -1, 0, 0, 0] надо вернуть None
		для [1, 1, 1, 1, -1, 1, 1, -1, 0, 0, 0] надо вернуть 1

"""

import random

"""
lst = []
for i in range (0,11):
    lst.append(random.randint(-1, 1))

print(lst, len(lst))

def calc_frequency(lst):

    frequency_lst = [0, 0, 0]
    max_frequency = 0
    most_frequent_nuber = None

    for elem in lst:

        if elem == 0:
            frequency_lst[0] += 1
            if frequency_lst[0] > max_frequency:
                max_frequency = frequency_lst[0]
                most_frequent_nuber = elem
        elif elem == 1:
            frequency_lst[1] += 1
            if frequency_lst[1] > max_frequency:
                max_frequency = frequency_lst[1]
                most_frequent_nuber = elem
        elif elem == -1:
            frequency_lst[2] += 1
            if frequency_lst[2] > max_frequency:
                max_frequency = frequency_lst[2]
                most_frequent_nuber = elem

    print(frequency_lst, most_frequent_nuber, max_frequency)

    if frequency_lst[0] == frequency_lst[1] or frequency_lst[1] == frequency_lst[2] or frequency_lst[0] == frequency_lst[2]:
        return None
    else:
        return most_frequent_nuber


print (calc_frequency(lst))
"""


lst = [random.randint(-1, 1) for i in range(11)]

print (lst)

def calc_frequency(lst):
    stats = [0, 0, 0]
    for elem in lst:
        stats[elem +1] += 1

    print (stats)

    if stats[0] > stats[1] and stats[0] > stats[2] and stats[1] != stats[2]:
        return -1
    elif stats[1] > stats[0] and stats[1] > stats[2] and stats[0] != stats[2]:
        return 0
    elif stats[2] > stats[0] and stats[2] > stats[1] and stats[0] != stats[1]:
        return 1
    else:
        return None

print (calc_frequency(lst))