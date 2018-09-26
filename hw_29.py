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
    low_case = 1
    upp_case = 3
    num = 2
    pass_length = 8


    password_lst = [random.randint(low_case, upp_case) for i in range(pass_length)]
    while low_case not in password_lst or upp_case not in password_lst or  num  not in password_lst:
        password_lst = [random.randint(low_case, upp_case) for i in range(pass_length)]

    for i in range (len(password_lst)):

        if password_lst[i] == low_case:
            password_lst[i] = small_letters[random.randint(0, len(small_letters)-1)]
        elif password_lst[i] == num:
            password_lst[i] = big_letters[random.randint(0, len(big_letters)-1)]
        elif password_lst[i] == upp_case:
            password_lst[i] = numbers[random.randint(0, len(numbers)-1)]

    password = ''.join(password_lst)

    return (password)

print (gen_password())


"""
[Biglbis/python_hw_Martyn] New comment on line 22 by dbradul on commit `6876e0e`
можно еще так:
```password_lst = [1, 2, 3]
password_lst += [random.randint(1, 3) for i in range(8) - len(password_lst)]```

[Biglbis/python_hw_Martyn] New comment on line 34 by dbradul on commit `6876e0e`
password = ''.join(password_lst)
"""