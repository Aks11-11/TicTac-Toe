board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

def play():
    game_is_still_on = True
    current_player = 'X'

    while game_is_still_on:
        displayboard()

        print(f"{current_player}'s turn")
        getinput(current_player)

        winner = check_winner()
        if not winner:
            current_player = switchplayer(current_player)
        else:
            displayboard()
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"{winner} won!")

            continue_to_play = input("Do you want to start another game (y/n): ")
            if continue_to_play.lower() == 'y':
                global board

                board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
                play()
            else:
                game_is_still_on = False

def displayboard():

    print(f"""
    {board[0]} | {board[1]} | {board[2]}
    {board[3]} | {board[4]} | {board[5]}
    {board[6]} | {board[7]} | {board[8]}
    """)


def getinput(current_player):

    choice = input("Select a position from 1-9: ")

    while True:
        if choice:
            if choice.isdigit():
                if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if board[int(choice) - 1] == '-':
                        board[int(choice) - 1] = current_player
                        break
                    else:
                        print("That position is already occupied!")
                else:
                    print("You can only select position between 1-9!")
            else:
                print("Your selection was invalid!")

            choice = input("Select a position from 1-9: ")
        else:
            print("You did not select a position!")
            choice = input("Select a position from 1-9: ")


def check_winner():
    global game_is_still_on
    winner = None

    if not winner:
        winner = check_row()

    if not winner:
        winner = check_column()

    if not winner:
        winner = check_diagonal()

    if not winner:
        winner = check_tie()

    return winner


def check_row():
    if board[0] == board[1] == board[2] != '-':
        return board[0]
    elif board[3] == board[4] == board[5] != '-':
        return board[3]
    elif board[6] == board[7] == board[8] != '-':
        return board[6]


def check_column():
    if board[0] == board[3] == board[6] != '-':
        return board[0]
    elif board[1] == board[4] == board[7] != '-':
        return board[1]
    elif board[2] == board[5] == board[8] != '-':
        return board[2]


def check_diagonal():
    if board[0] == board[4] == board[8] != '-':
        return board[0]
    elif board[2] == board[4] == board[6] != '-':
        return board[2]


def check_tie():
    if '-' not in board:
        return 'Tie'

def switchplayer(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'

play()