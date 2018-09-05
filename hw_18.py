"""
Каждому символу в таблице символов Unicode соответствует число.
Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам,
стоящим между двумя заданными включительно.
Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.
		def sum_symbol_codes(first, last): # returns int
			pass
"""

def sum_symbol_codes(first, last):
    kod_first = ord(first)
    kod_last = ord(last)
    kod_sum = 0
    for i in range(kod_first,kod_last+1):
        kod_sum += i
    return kod_sum

print ('Sum = ', sum_symbol_codes('x','z'))
