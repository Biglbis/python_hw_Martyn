"""
Написать функцию решения квадратного уравнения.
		def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots, 1 root and None or 2 Nones
"""
import math

def solve_quadratic_equation (a, b, c) :

    d = b**2 - 4*a*c

    #print(d)

    if d == 0:
        x = (- b) / (2 * a)
        return x, None

    elif d < 0:
        return None, None

    elif d > 0:
        x1 = (- b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (- b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return x1, x2


print(solve_quadratic_equation(2, 4, 2))

