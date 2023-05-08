# generate a random number between 1 and 10
# ask user for input
# check the input for an int
# check they guessed correctly
from random import randint

rand_num = randint(1, 10)
while True:
    try:
        guess = int(input('Guess a number between 1 and 10 '))
        if guess == rand_num:
            print('You won!')
            break
        else:
            print('Try again.')
    except:
        print('Oops. Please enter a number.')

# Below is my attempt without pseduo code
# class RandomGame:
#     run = True
#     while run:
#         try:
#             print('What number range do you want to play?')
#             num1 = int(input())
#             num2 = int(input())
#             rand = randint(num1, num2)
#             print(f'Okay! Between {num1} and {num2}, what is your guess?')
#             while True:
#                 guess = int(input())
#                 if guess == rand:
#                     print('Congrats! You won the game!')
#                     run = False
#                     break
#                 else:
#                     print('Not quite. Guess again.')
#         except:
#             print('Oops. Please enter a number.')
