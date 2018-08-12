"""
Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase.
Для простоты считаем, что имя переменной всегда состоит из 3-х слов.
Например: 'employee_first_name' -> 'EmployeeFirstName'
"""
snake_case = 'employee_first_name'
snake_case_lst = snake_case.split('_')
print(snake_case_lst)
word_1 = snake_case_lst[0]
word_2 = snake_case_lst [1]
word_3 = snake_case_lst [2]
print(word_1, word_2, word_3)
CamelCase = word_1.capitalize()+word_2.capitalize()+word_3.capitalize()
print('For snake_case <', snake_case, '> CamelCase will be: <', CamelCase, '>')


