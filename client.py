# CHRISTIAN RIVA
# EWA GIERLACH
#
#
import time
from TicTacToeClientConnection import TicTacToeClientConnection
from tabulate import tabulate
from GuessNumberConnection import GuessNumberConnection

HOST = 'localhost'
PORT = 50007

playername = input("insert your name: ")
while True:
    try:
        which_game = int(input("TicTacToe [1] or GuessNumber [2]: "))
        if not (which_game is 1 or which_game is 2):
            raise ValueError
        break
    except ValueError or TypeError:
        print("Wrong value! Put 1 or 2")
if which_game == 1:
    while True:
        try:
            number_of_player = int(input("Singleplayer [1] or Multiplayer [2]: "))
            if not (number_of_player is 1 or number_of_player is 2):
                raise ValueError
            connection = TicTacToeClientConnection(HOST, PORT)
            break
        except ValueError or TypeError:
            print("Wrong value! Put 1 or 2")
else:
    number_of_player = 1
    connection = GuessNumberConnection(HOST, PORT)
if connection.connect()==1:
    print("Connected succesfully")
    connection.initial_settings(number_of_player,playername,which_game)
    if which_game == 1:
        if number_of_player == 1:
            while connection.status_of_the_match() == 0:
                print(tabulate(connection.battlefield_request(), tablefmt="grid"))
                if connection.get_next() == 1:
                    while True:
                        try:
                            choice = int(input(playername + " it's your turn. Put your choice (1-9): \n"))
                            if choice > 9 or choice < 1:
                                raise ValueError
                        except ValueError or TypeError:
                            print("Wrong value! Print an integer in range (1-9)")
                            continue
                        if connection.is_free(choice):
                            connection.put_choice(1, choice)
                            break
                        print("That position is already taken")
                elif connection.get_next() == 2:
                    connection.computer_turn()
                #the game is finished
            print(tabulate(connection.battlefield_request(), tablefmt="grid"))
            winner = connection.status_of_the_match()
            if winner == 1:
                print(playername+" won this game!!!!!")
            elif winner == 2:
                print("computer won this game!!!!!")
            else:
                print("Nobody won this match ¯\_(ツ)_/¯ ")
            time.sleep(3)
            connection.close_connection()
        elif number_of_player == 2:
            raise NotImplementedError  # NOT IMPLEMENTED YET
    elif which_game == 2:
        print("Welcome!, I will take an integer from range of 0 to 100. Try to guess this number!")
        while True:
            inp = input('Type your guess, or type "quit" to quit\n')
            if inp == "quit":
                break
            connection.give_input(inp)
            response = connection.get_response()
            if response[0] == 2:
                print(response[1])
                break
            elif response[0] == 1:
                print(response[1])
            else:
                print(response)
        time.sleep(3)
        connection.close_connection()
        #raise NotImplementedError  # NOT IMPLEMENTED YET


