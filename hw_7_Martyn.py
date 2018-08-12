"""
Преобразовать строку с американским форматом даты в европейский.
Например, '05.17.2016' преобразуется в '17.05.2016'
"""
date = '05.17.2016'
date_lst = date.split('.')
print('For american date style %s, in euro date style will look like %s.%s.%s'
      % (date, date_lst[1], date_lst[0], date_lst[2]))



