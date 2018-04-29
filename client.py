# CHRISTIAN RIVA
# EWA GIERLACH
#
#
from TicTacToeClientConnection import TicTacToeClientConnection
from tabulate import tabulate
from GuessNumberConnection import GuessNumberConnection
import socket, pickle

HOST = 'localhost'
PORT = 10009

playername = input("insert your name: ")
which_game = int(input("TicTacToe [1] or GuessNumber [2]: "))
if which_game == 1:
    number_of_player = int(input("Singleplayer [1] or Multiplayer [2]: "))
    connection = TicTacToeClientConnection(HOST, PORT)
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
                        choice = int(input(playername + " it's your turn. Put your choice (1-9): \n"))
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
            #close connection:
            connection.close_connection()
        elif number_of_player == 2:
            raise NotImplementedError  # NOT IMPLEMENTED YET
    elif which_game == 2:
        print("Welcome!, I will take an integer from range of 0 to 100. Try to guess this number!")
        while 1:
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
        connection.close_connection()
        #raise NotImplementedError  # NOT IMPLEMENTED YET


