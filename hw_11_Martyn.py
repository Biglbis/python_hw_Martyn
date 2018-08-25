"""
Написать функцию, которая будет переводить градусы в радианы (без использования math.radians).
Используя эту функцию, вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
def degrees2radians(degrees): # returns float
"""

import math
a=60
b=45
c=40

def degrees2radians(degrees):
    result = degrees * math.pi / 180
    return result

rad_a = degrees2radians(a)
rad_b = degrees2radians(b)
rad_c = degrees2radians(c)

cos_a = math.cos(rad_a)
cos_b = math.cos(rad_b)
cos_c = math.cos(rad_c)

print ('Cos of angles %d,%d,%d  degrees is %f, %f, %f radians' %(a, b, c, cos_a, cos_b, cos_c))

