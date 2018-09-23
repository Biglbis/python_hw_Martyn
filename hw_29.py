"""
Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
Пароль состоит из 8 символов
В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
Пароль обязательно должен содержать Большие и маленькие буквы и цифры

def gen_password(): # returns string
			pass
"""


import random

def gen_password():
    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    password = ''

    password_lst = [random.randint(1, 3) for i in range(8)]
    while 1 not in password_lst or 2 not in password_lst or  3  not in password_lst:
        password_lst = [random.randint(1, 3) for i in range(8)]

    for i in range (len(password_lst)):

        if password_lst[i] == 1:
            password_lst[i] = small_letters[random.randint(0, len(small_letters)-1)]
        elif password_lst[i] == 2:
            password_lst[i] = big_letters[random.randint(0, len(big_letters)-1)]
        elif password_lst[i] == 3:
            password_lst[i] = numbers[random.randint(0, len(numbers)-1)]

    for char in password_lst:
        password += char

    return (password)

print (gen_password())