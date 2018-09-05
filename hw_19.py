"""
Написать функцию для поиска разницы между максимальным и минимальным числом среди
num_limit случайно сгенерированных чисел в указанном числовом диапазоне.
		def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
			pass
"""

import random

def diff_min_max(num_limit, lower_bound, upper_bound):
    min_num = upper_bound
    max_num = lower_bound
    for i in range (num_limit):
        num = random.randint(lower_bound,upper_bound)
        print (num)
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    print('min =', min_num)
    print('max =', max_num)
    difference = max_num - min_num
    return difference

print('Difference = ' , diff_min_max(10, 1, 50))