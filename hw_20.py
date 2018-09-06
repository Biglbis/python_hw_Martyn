"""
Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел
среди num_limit случайно сгенерированных чисел в указанном числовом диапазоне.
Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
		def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
		     pass
"""

import random

def diff_even_odd(num_limit, lower_bound, upper_bound):
    sum_even = 0
    sum_odd = 0
    for i in range (num_limit):
        num = random.randint(lower_bound,upper_bound)
        print (num)
        if num %2 == 0:
            sum_even += num
        else:
            sum_odd += num
    print('Sum even =', sum_even)
    print('Sum odd =', sum_odd)
    difference = sum_even - sum_odd
    return difference

print('Difference = ' , diff_even_odd (10, 1, 50))