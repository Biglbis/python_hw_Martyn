"""
Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
После чего опять просит угадать. И так пока пользователь не угадает выбранное число.
"""
import random

comp_choice = random.randint (1, 10)
print('Guess a number from 1 to 10 !!! (\'q\'  for exit): ')

while True:
    user_choice = input ('Your choice: \n')
    if user_choice == 'q':
        break

    if not user_choice.isnumeric():
        print ('Invalid data')
        continue

    if not 1 <= int(user_choice) <= 10:
        print ('Invalid data')
        continue

    if int(user_choice) == comp_choice:
        print ('Great! You won!')
        break
    else:
        if int(user_choice) > comp_choice:
            print ('Your choice is bigger. Try again')
        else:
            print('Your choice is smaller. Try again')
