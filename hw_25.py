"""
Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию,
которая переставляет его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
	Примечание: использовать метод random.shuffle не допускается.

     def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
		pass
"""

import random

lst_odd = []
for i in range (1,100):
    if (i % 2) != 0:
        lst_odd.append(i)

def shuffle_list(list_to_shuffle):
    for i in range (0, len(list_to_shuffle)):
        random_index = random.randint (0, (len(list_to_shuffle)-1))
        temp_elem = list_to_shuffle[i]
        temp_random = list_to_shuffle[random_index]
        list_to_shuffle[i] = temp_random
        list_to_shuffle[random_index] = temp_elem
    print (list_to_shuffle)

shuffle_list(lst_odd)
