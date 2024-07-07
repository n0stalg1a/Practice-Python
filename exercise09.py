# 9: Guessing Game One
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, 
# too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, 
# print this out.

import random


def game():
    num = random.randint(1, 9)

    print('I have chosen a random number 1 through 9. Can you guess it? ')

    guesses = 0

    while True:
        guess = input('Enter a guess OR type exit: ')
        if guess == 'exit':
            print('Exiting.')
            exit()
        else:
            guess = int(guess)
            pass

        if guess == num:
            guesses += 1
            print(f'\nYou Win! The random number I chose was indeed {num}.')
            print(f'It took you {guesses} guesses.\n\n')
            game()
        elif guess < num:
            guesses += 1
            print('Too low.')
        else:
            guesses += 1
            print('Too high.')

game()