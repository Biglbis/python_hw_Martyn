"""
Написать функцию, возвращающую все простые числа от 1 до 100 в виде списка.
def gen_primes(): # returns list of ints
			pass
"""

def gen_primes():
    lst = [i for  i in range (2, 100)  if i == 2 or i == 3 or i== 5 or i== 7 or i%2 != 0 and i %3 != 0 and i %5 != 0 and i%7 != 0]

    return lst


print (gen_primes())

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,