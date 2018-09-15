"""
Разобраться с Enum и переписать игру с его использованием.
"""

import random
import enum

GREETING = """
Enter data 
    1 - ROCK
    2 - PAPER
    3 - SCISSORS
   (press 'q'  for exit):
"""

class Choice (enum.Enum):
   ROCK = 1
   PAPER = 2
   SCISSORS = 3

'''
def code2text(code):
    if code == ROCK:
        return 'ROCK'
    elif code == PAPER:
        return 'PAPER'
    elif code == SCISSORS:
        return 'SCISSORS'
'''

def who_is_winner (pc_choice, user_choice):
   if pc_choice == Choice.ROCK.value and user_choice == Choice.SCISSORS.value:
     return False
   if pc_choice == Choice.PAPER.value and user_choice == Choice.ROCK.value:
     return False
   if pc_choice == Choice.SCISSORS.value and user_choice == Choice.PAPER.value:
     return False
   return True

def game ():

    while True:
        input_data = input(GREETING)
        if input_data == 'q':
            break

        if not input_data.isnumeric():
            print('Invalid data')
            continue

        if not 1 <= int(input_data) <= 3:
            print('Invalid data')
            continue

        user_choise = int (input_data)
        print('User choice is:', Choice(user_choise).name)

        pc_choice = random.randint (Choice.ROCK.value, Choice.SCISSORS.value)
        print ('PC choice is:', Choice(pc_choice).name)

        if pc_choice == user_choise:
            print ('Wow! It is Tie')

        else:
            if who_is_winner (pc_choice, user_choise):
                print ('Congratulations! You won!')

            else:
                print('Ooops. You loose! Try again!')


game()