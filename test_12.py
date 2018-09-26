import random

def summer_test():
    temp_lst  = ['i', ' ', '*', ' ', 'j', ' ', '=']
    full_lst = []
    for i in range (2, 10):
        for j in range (i, 10):

            temp_lst[0] = str (i)
            temp_lst[4] = str (j)
            temp_str = ''.join(temp_lst)
            full_lst.append(temp_str)


    lst_15 = []
    for i in range (1, 16):
        n = random.randint (0, len (full_lst))
        lst_15.append(full_lst[n])

    return lst_15

print (summer_test())