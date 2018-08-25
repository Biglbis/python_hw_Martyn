"""
13.	Написать функцию, которая вычислит площадь и объем конуса по его радиусу и высоте.
Результат работы функции должен вернуть два значения.
def cone_square_and_volume(radius, height): # returns 2 floats
"""
import math
radius = 5
height = 20

def cone_square_and_volume(radius, height):
    l = math.sqrt(height**2 + radius**2)
    square = math.pi * radius * l + math.pi * radius**2
    volume = 1/3 * math.pi * radius**2 * height
    return square,volume

square, volume = cone_square_and_volume(radius, height)

print ('For cone with radius %d, and height %d, \n Cone square = %.2f, Cone volume = %.2f'
       %(radius, height, square,volume))
