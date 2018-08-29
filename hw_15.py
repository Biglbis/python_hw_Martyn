"""
Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
Каждая окружность задается координатами центра и радиусом.
def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
"""
import math
def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt ((x2-x1)**2 + (y2-y1)**2)
    if d < math.fabs((r1-r2)) or d > r1 + r2 :
        return False
    else:
        return True

print ('Is there intersection? ', circles_intersect(0,0,5,0,0,4))


