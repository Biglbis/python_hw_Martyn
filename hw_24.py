"""
Для удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы
в зависимости от первых букв их фамилии.
Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’.
Название группы определяет в какую группу попадает абитуриент, в зависимости от первой буквы его/ее фамилии.
Например, Will Smith попадает в группу ‘Q-T’,
т.к. первая буква его фамилии попадает в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).
Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д.
Написать функцию, которая получает список имен студентов вида
['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...] и возвращает количество абитуриентов в группах,
сформированных по их фамилиям, описанным выше образом.

     def group_by_surname(list_of_enrollees): # returns 4 ints
			pass
"""

students = ['A I', 'B J', 'C T', 'D U']

def group_by_surname(list_of_enrollees):
    group_1 = 0
    group_2 = 0
    group_3 = 0
    group_4 = 0

    for elem in list_of_enrollees:
        student = elem.split(' ')
        surname = student[1]
        first_letter_code = ord(surname[0])

        if ord ('A') <= first_letter_code <= ord ('I'):
            group_1 += 1
        elif ord ('J') <= first_letter_code <= ord ('P'):
            group_2 += 1
        elif ord ('Q') <= first_letter_code <= ord ('T'):
            group_3 += 1
        elif ord ('U') <= first_letter_code <= ord ('Z'):
            group_4 += 1
    return (group_1, group_2, group_3, group_4)

print (group_by_surname(students))