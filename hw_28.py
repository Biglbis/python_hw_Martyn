"""
Создать программу, которая запрашивает у пользователя произвольную строку символов.
Далее программа ее шифрует и выводит на экран в зашифрованном виде.
Шифрование происходит путем замены каждого символа символом, который находится на 5 позиций правее
в предопределенной таблице шифрования.
Таблица шифрования задается программистом в виде одномерного списка символов
латинского алфавита от a до z и цифр от 0 до 9.
Если при выборе символа для шифровки таблица шифрования заканчивается, то циклически переходить к ее началу.
Отсутствующие в таблице шифрования символы, записываются в результирующую строку без изменений.
Регистр игнорируется.
	Таблица шифрования (a, b, c, d, ..., x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	Например: Исходная строка, которую ввел пользователь: 'secret', 'office 365'
	Зашифрованная строка, которую выдала программа: 'xjhwjy', 'tkknhj 8ba'
	Примечание: т.н. таблица шифрования может быть представлена как строка или список.

def encode(str_to_encode): # returns enсoded string
		pass
"""
import string
print (string.ascii_letters)

input_string = input ('Enter sting:',)
print (input_string)


def encode(str_to_encode):
    encode_table = 'abcdefghijklmnopqrstuvwxyz0123456789'
    input_lst = []
    encoded_string = ''

    for char in str_to_encode:
        input_lst.append(char)


    for i in range (len(input_lst)):
        if input_lst[i] in encode_table:
            idx = encode_table.find(input_lst[i])
            new_idx = (idx + 5) % len(encode_table)
            coded_char = encode_table[new_idx]

            input_lst[i] = coded_char


    for char in input_lst:
        encoded_string += char

    return (encoded_string)


print(encode(input_string))


"""
[Biglbis/python_hw_Martyn] New comment on line 32 by dbradul on commit
можно так:
```input_lst = [char for char in str_to_encode]```

или даже так:
```input_lst = list(str_to_encode)```

[Biglbis/python_hw_Martyn] New comment on line 45 by dbradul on commit
encoded_str = ''.join(input_lst)
"""

