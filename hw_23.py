"""
Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи
незначительную, на первый взгляд, награду:
столько пшеничных зёрен, сколько окажется на шахматной доске,
если на первую клетку положить одно зерно, на вторую — два зерна, на третью — четыре зерна и т. д.
Оказалось, что такого количества зерна нет на всей планете (оно равно 2**64 − 1 зерен).
Посчитайте, начиная с какой клетки по счету, общее количество зерен,
которое должен был бы отдать раджа изобретателю было больше 1 000 000 зерен
и сколько конкретно зерен он должен был бы отдать.
     def chess_reward(): # returns 2 ints (cell number and total number of corns)
		pass
"""

def chess_reward():
    cell_number = 1
    total_number_of_corns = 0

    while cell_number <= 64 :
        corns_per_cell = 2 ** (cell_number - 1)
        total_number_of_corns += corns_per_cell

        if total_number_of_corns > (10 ** 6):
            break

        cell_number += 1

    print (' One mil corns cell = %d  \n Total corns number = %d' % (cell_number, total_number_of_corns))
    return (cell_number, total_number_of_corns)

chess_reward()



