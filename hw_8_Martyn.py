"""
Дана строка с именем студента, в которой имя предшествует фамилии, например  ‘Mark Zuckerberg‘.
Написать программу, которая преобразует эту строку, ставя фамилию на первое место, а имя на второе.
Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.
"""
name = 'Mark Zuckerberg'
name_idx = name.find(' ')
new_name = name[name_idx:] + ' ' + name[:name_idx]
print(name, 'is the same as', new_name)


