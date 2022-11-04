#from IPython.display import clear_output
import random

# Print the Board

board_list = ['#','X','X','X','X','X','X','X','X','X']
def board(board_list):
#   clear_output()       FOR JUPITER NOTEBOOKS
    print("\n"*100)
    print('   |   |')
    print(' ' + board_list[7] + ' | ' + board_list[8] + ' | ' + board_list[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board_list[4] + ' | ' + board_list[5] + ' | ' + board_list[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board_list[1] + ' | ' + board_list[2] + ' | ' + board_list[3])
    print('   |   |')
# Take Input and Verify

def input_given():
    
    #Player 1
    choice = ''
    while choice != "X" and choice != "O":
        choice = input("Let's see who goes first - Choose X or O:")
    
    player1 = choice
    #Player 2
    
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1,player2)

#Feed Input to the board

def feed_input(board_list,choice,position):
    board_list[position] = choice

# Check the Result

def result(board_list,option):
    return ((board_list[7] == option and board_list[8] == option and board_list[9] == option)or 
    (board_list[4] == option and board_list[5] == option and board_list[6] == option)or
    (board_list[1] == option and board_list[2] == option and board_list[3] == option)or
    (board_list[1] == option and board_list[5] == option and board_list[9] == option)or
    (board_list[7] == option and board_list[5] == option and board_list[3] == option)or
    (board_list[7] == option and board_list[4] == option and board_list[1] == option)or
    (board_list[8] == option and board_list[5] == option and board_list[2] == option)or
    (board_list[9] == option and board_list[6] == option and board_list[3] == option))

# Toss to see which player goes first

def toss():
    flip = random.randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

# Check if there's an empty space available on the board
def space_check(board_list,postion):
    return board_list[postion] == ' '

# To check if the board is full or not[Boolean]
def board_check(board_list):
    for i in range(1,10):
        if space_check(board_list,i):
            return False
    return True
    
# Ask for the position of element from user

def position_choice(board_list):
    position = 0
    while position not in range(1,10) or not space_check(board_list,position):
        position = int(input("Choose the position for your move(1-9)\n P.S Starting from Bottom-Left."))
    
    return position

# Ask the user if they wanna play again

def play_again():
    play_choice = input("You wanna Play Again? Type YES or NO")
    return play_choice == "YES"


# Final Run
print("Hi! Welcome to Tic-Tac-Toe!!")

while True:
    # Reset the board
    boardlist = [' '] * 10
    player1_marker, player2_marker = input_given()
    turn = toss()
    print(turn + ' will go first.')
    
    start_playing = input('Ready to play? ("Y/N")')
    
    if start_playing.lower()[0] == 'y':
        start_game = True
    else:
        start_game = False

        #Actual Gameplay

    while start_game:
        if turn == "Player 1":
            # Player1's turn.
            
            board(boardlist)
            position = position_choice(boardlist)
            feed_input(boardlist, player1_choice, position)

            if result(boardlist,player1_choice):
                board(boardlist)
                print("Player 1 Won !!")
                start_game = False
            else:
                if board_check(boardlist):
                    board(boardlist)
                    print('Its a TIE!!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            board(boardlist)
            position = position_choice(boardlist)
            feed_input(boardlist,player2_choice,position)

            if result(boardlist,player2_choice):
                board(boardlist)
                print("Player 2 Won !!")
                start_game = False
            else:
                if board_check(boardlist):
                    board(boardlist)
                    print("Its a TIE!!")
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break
            
