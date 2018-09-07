"""
Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
a) c использованием строк, b) без использования строк.
def get_max_digit(number): # returns int
		     pass
"""

import random

print('A')
def get_max_digit_a(number):
    print(number)
    num_str = str(number)
    max_num = int (num_str[0])
    for char in num_str:
        if int(char) > max_num:
            max_num = int(char)
    return max_num

print ('Max digit =', get_max_digit_a(random.randint(10**11, 10**12)))


print('B')

def get_max_digit_b(number):
    print(number)
    max_num = number %10

    for i in range (0, 12):
        digit = number % 10
        if digit > max_num:
            max_num = digit
        number = number // 10

    return max_num


print ('Max digit =', get_max_digit_b(random.randint(10**11, 10**12)))
