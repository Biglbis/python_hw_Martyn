"""
Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
введенного пользователем в консоли, без использования операторов цикла.
a) cо строками, б) без использования строк.
def sum_of_digits(number): # returns int
"""
number_str = input('Enter number:')

#a
def sum_of_digits_a(number):
    n1 = number_str[0]
    n2 = number_str[1]
    n3 = number_str[2]
    result = int(n1) + int(n2) + int(n3)
    return result

result = sum_of_digits_a(number_str)
print(result)

#b

number = int(number_str)

def sum_of_digits_b (number):
    n1 = number %10
    n2 = (number // 10) % 10
    n3 = number // 100
    result = n1+n2+n3
    return result

result1= sum_of_digits_b(number)
print (result1)

