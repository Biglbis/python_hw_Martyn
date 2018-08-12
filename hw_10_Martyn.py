"""
Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'.
В этой строке указаны имя писателя и через символ * даты рождения и смерти.
Даты указаны в формате "YYYY-MM-DD".
Требуется написать программу, которая по переданной строке определит возраст писателя и распечает его имя и возраст.
Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна распечает: 'Leo Tolstoy, 82'.
Для строки 'Marcus Aurelius*121-04-26*180-03-17' - 'Marcus Aurelius, 59'.
Примечание: Т.к. имена писателей могут быть разной длины, то индексы символов разделителей ('*', '-') будут разными!
Месяцы и дни для определения возраста можно игнорировать.
"""
writer = 'Marcus Aurelius*121-04-26*180-03-17'
writer_lst = writer.split('*')
writer_name = writer_lst[0]
birthday = writer_lst[1]
death = writer_lst[2]
birthday_lst = birthday.split('-')
death_lst = death.split('-')
year_of_birth = int(birthday_lst[0])
year_of_death = int(death_lst[0])
age = year_of_death - year_of_birth
print (writer_name, 'died at the age of', age)


