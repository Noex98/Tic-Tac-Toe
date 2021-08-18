import random
game_position = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
game_turn = 0
game_players = ['X', 'O']
game_board = '''

|----|----|----|
| {game_position[0]}  | {game_position[1]}  | {game_position[2]}  |
|----|----|----|
| {game_position[3]}  | {game_position[4]}  | {game_position[5]}  |
|----|----|----|
| {game_position[6]}  | {game_position[7]}  | {game_position[8]}  |
|----|----|----|

'''
def print_board(played_by):
    print('\nTurn {game_turn}: {played_by}'.format(game_turn = game_turn, played_by = played_by))
    print(game_board.format(game_position = game_position))

def game_end(winner):
    if player_is == winner:
        print('''
    ################################
    #                              #
    #  Congratiolations, you won!  #
    #                              #
    ################################
        ''')
    elif 'tie' == winner:
        print('''
    ##############################
    #                            #
    #  It was a tie, try again!  #
    #                            #
    ##############################
        ''')
    else:
        print('''
    ###############################################
    #                                             #
    #  You lost this one, better luck next time!  #
    #                                             #
    ###############################################
        ''')
    

def detect_end():
    for player in game_players:
        # Horizontal win
        if (game_position[0] == player and game_position[1] == player and game_position[2] == player) or (game_position[3] == player and game_position[4] == player and game_position[5] == player) or (game_position[6] == player and game_position[7] == player and game_position[8] == player):
            game_end(player)
            return 'end'
        # Vertical win
        elif (game_position[0] == player and game_position[3] == player and game_position[6] == player) or (game_position[1] == player and game_position[4] == player and game_position[7] == player) or (game_position[2] == player and game_position[5] == player and game_position[8] == player):
            game_end(player)
            return 'end'
        # Diagonal win
        elif (game_position[0] == player and game_position[4] == player and game_position[8] == player) or (game_position[2] == player and game_position[4] == player and game_position[6] == player):
            game_end(player)
            return 'end'
    if ' ' not in game_position:
        game_end('tie')
        return 'end' 


def player_turn():

    global game_turn
    game_turn += 1
    
    def player_input():
        row = int(input('Pick a row (1, 2 or 3): ')[0])
        column = int(input('Pick a column (1, 2 or 3): ')[0])
        if game_position[(row - 1) * 3 + column - 1] != ' ':
            print('\nThat position is already occupied, try again\n')
            player_input()
        else:
            game_position[(row - 1) * 3 + column - 1] = player_is

    player_input()
    
    print_board('Player')

    if detect_end() != 'end':
        py_turn()

def py_turn():
    n = random.randint(0, 8)

    if game_position[n] == 'X' or game_position[n] == 'O':
        py_turn()
    else:
        global game_turn
        game_turn += 1
        if player_is == 'X':
            game_position[n] = 'O'
            print_board('Python')
        else:
            game_position[n] = 'X'
            print_board('Python')
        if detect_end() != 'end':
            player_turn()


# Intro

print('''
Tic Tac Toe

How to play:

1. Choose whether you want to start or not (X will always start)
2. To play a mark, choose a column (1, 2 or 3), then choose a row (1, 2 or 3)
3. Have fun ;)
''')

input('Press enter to continue\n')

# Choose X or O

def start_select():
    start = input('Do you wish to place the first mark? (y/n): ')[0].lower()
    global player_is

    if start == 'y':
        player_is = 'X'
        print_board('')
        player_turn()
    elif start == 'n':
        player_is = 'O'
        print_board('')
        py_turn()
    else:
        print('\n\nUnexpected input, please write y or n \n')
        start_select()

start_select()