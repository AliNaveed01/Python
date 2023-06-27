# here we will create rock paper scissors game using python

import random

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def play():
    # now we will take input from the user
    #turn = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n: ")
    userturn = random.choice(['r', 'p', 's'])
    
    choice = "y"
    
    while choice == 'y':
        turn = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n: ")
        if turn == userturn:
            print( "It's a tie!")
        
        elif is_win(turn, userturn):
            print( "You won!")
        
        else:
            print("You lost!")
            
        choice = input("Do you want to play again? (y/n): ")
        
print(play())