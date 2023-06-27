import math
import random  
import time

class Player:
    def __init__(self, letter):
        self.letter = letter # letter is X or O
        
    def get_moves(self, game):
        pass
        

class CompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_moves(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_moves(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')
            
        return val
    def play(game, x_player, o_player, print_game=True):
        # returns the winner of the game(the letter) or None for a tie
        if print_game:
            game.print_board_nums()
        
        letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)
        while game.empty_squares():
            # get the move from the appropriate player
            if letter == 'O':
                square = o_player.get_moves(game)
            else:
             square = x_player.get_moves(game)
            
            # let's define a function to make a move!
            if game.make_move(square, letter):
                if print_game:
                    print(letter + ' makes a move to square {}'.format(square))
                    game.print_board()
                    print('') # just empty line
                
                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter
            
                # after we made our move, we need to alternate letters
                letter = 'O' if letter == 'X' else 'X' # switches player
            
            # tiny break to make things a little easier to read
            if print_game:
                time.sleep(0.8)
        
        if print_game:
            print('It\'s a tie!')
    
    

