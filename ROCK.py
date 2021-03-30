import random
moves = ['ROCK', 'PAPER', 'SCISSORS']
player1 = input('enter either rock,paper or scissors >> ')
computer = random.choice(moves)
play = True

while play == True:

    if player1 == 'ROCK' and computer == 'SCISSORS' :
        print('player1 wins this round')
        print(computer)
        play = False

    elif player1 == 'ROCK' and computer == 'ROCK' :
        print("it's a draw")
        print(computer)
        play = False
    elif player1 == 'ROCK' and computer == 'PAPER':
        print('the computer won this match')
        print(computer)
        play = False
    elif player1 == 'SCISSORS' and computer == 'ROCK':
        print('the computer won')
        print(computer)
        play = False
    elif player1 == 'SCISSORS' and computer == 'PAPER':
        print('player1 wins this match')
        print(computer)
        play = False
    elif player1 == 'SCISSORS' and computer == 'SCISSORS':
        print("it's a draw")
        print(computer)
        play = False
    elif player1 == 'PAPER' and computer == 'ROCK':
        print('player1 wins the match')
        print(computer)
        play = False
    elif player1 == 'PAPER' and computer == 'SCISSORS':
        print('the computer wins this match')
        print(computer)
        play = False
    elif player1 == 'PAPER' and computer == 'PAPER':
        print("it's a draw")
        print(computer)
        play = False

print('The match is over...')
