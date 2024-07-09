# 8: Rock Paper Scissors
# Make a two-player Rock-Paper-Scissors game.

import random

playerwins = 0
computerwins = 0
draws = 0


def playagain():
    playerchoice = input('Would you like to play again? y or n: ')
    if playerchoice == 'y':
        print(f'Current Score:- \nPlayer wins {playerwins}\nComputer wins'
              f' {computerwins}\nDraws {draws}')
        game()
    else:
        print(f'End Score:- \nPlayer wins {playerwins}\nComputer wins'
              f' {computerwins}\nDraws {draws}')
        quit()


def game():
    global playerwins
    global computerwins
    global draws

    # The exercise didnt ask for this I just did it to automate the choices
    # for the computer and player
    actions = ['rock', 'paper', 'scissors']
    playerchoice = random.choice(actions)
    computerchoice = random.choice(actions)

    print(f'Player chose: {playerchoice}')
    print(f'Computer chose: {computerchoice}')

    if playerchoice == computerchoice:
        print('Draw!')
        draws += 1
        playagain()
    elif playerchoice == 'rock' and computerchoice == 'paper':
        print(f'Computer wins {computerchoice} wraps {playerchoice}.')
        computerwins += 1
        playagain()
    elif playerchoice == 'paper' and computerchoice == 'scissors':
        print(f'Computer wins {computerchoice} cuts {playerchoice}.')
        computerwins += 1
        playagain()
    elif playerchoice == 'scissors' and computerchoice == 'rock':
        print(f'Computer wins {computerchoice} smashes {playerchoice}.')
        computerwins += 1
        playagain()
    elif playerchoice == 'rock' and computerchoice == 'scissors':
        print(f'You win! {playerchoice} smashes {computerchoice}')
        playerwins += 1
        playagain()
    elif playerchoice == 'paper' and computerchoice == 'rock':
        print(f'You win! {playerchoice} wraps {computerchoice}')
        playerwins += 1
        playagain()
    elif playerchoice == 'scissors' and computerchoice == 'paper':
        print(f'You win! {playerchoice} cuts {computerchoice}')
        playerwins += 1
        playagain()
    else:
        print('You should never get here!')
        playagain()

game()
