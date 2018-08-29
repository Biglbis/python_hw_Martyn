"""
Два поезда движутся на скорости V1 и V2 навстречу друг другу.
Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
При заданных скоростях узнать столкнутся ли поезда.
def have_trains_crashed(v1, v2): # returns boolean value
"""

def have_trains_crashed(v1, v2):
    return 4 / v1 >= 6 / v2
print ('Will trains crash? ', have_trains_crashed(2,3))
