import socket, pickle
from tabulate import tabulate
from TicTacToe import TicTacToe
from GuessNumber import GuessNumber

def p2pServer(playername):
    HOST = input("Your IP: (If you are connecting locally, press enter)")
    PORT = input("Give the PORT: (If you just press enter, the default value is 50008)")

    if HOST == "\n" or " \n":
        HOST = "localhost"
    try:
        PORT = int(PORT)
    except ValueError:
        PORT = 50008

    which_game = 1

    print("WAITING FOR CONNECTION")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)

    conn, addr = s.accept()

    print('Connected by', addr)
    conn.send(pickle.dumps(1))

    while 1:
        data = conn.recv(4096)
        if data:
             #conn.send(data)
            data_arr = pickle.loads(data)

            if data_arr[0] == 1:
                 #GAME INITIALIZATION:
                which_game = data_arr[3]
                if which_game == 1:
                    print("STARTING TIC TAC TOE") #############################
                    game = TicTacToe()
                    game.set_name_player1(data_arr[2])

                    game.set_name_player2(playername)

                    SERVER_STATUS = 1
                    break
    while SERVER_STATUS == 1:
        data = conn.recv(4096)
        if data:
            # conn.send(data)
            data_arr = pickle.loads(data)

            if data_arr[0] == 2:
                    #request battlefield
                conn.send(pickle.dumps([2, game.get_battlefield()]))

            elif data_arr[0] == 3:
                    #put choice
                game.put_choice(data_arr[1],data_arr[2])
                conn.send(pickle.dumps([3,1]))
            elif data_arr[0] == 4:
                #status of the match
                status = game.status_of_the_match()
                if status != 0:
                    print("game is ended")
                conn.send(pickle.dumps([4,status]))
            elif data_arr[0] == 42:
                #status of the match
                status = game.status_of_the_match()
                if status != 0:
                    message  = data_arr[1]
                    print(message)
                    print("game is ended")
                conn.send(pickle.dumps([4,status]))
            elif data_arr[0] == 5:
                #get next
                conn.send(pickle.dumps([5, game.get_next()]))

            elif data_arr[0] == 6:
                #is free
                conn.send(pickle.dumps([6, game.is_free(data_arr[1])]))

            elif data_arr[0] == 7:
                print(tabulate(game.get_battlefield(), tablefmt="grid"))
                while True:
                    try:
                        choice = int(input(game.player2_name + " it's your turn. Put your choice (1-9): \n"))
                        if choice > 9 or choice < 1:
                            raise ValueError
                    except ValueError or TypeError:
                        print("Wrong value! Print an integer in range (1-9)")
                        continue
                    if game.is_free(choice):
                        game.put_choice(2, choice)
                        break
                    print("That position is already taken")
                conn.send(pickle.dumps([7]))
                print(tabulate(game.get_battlefield(), tablefmt="grid"))
            elif data_arr[0] == -1:
                #CLOSE CONNECTION
                print("CONNECTION CLOSED")
                SERVER_STATUS = 0
                conn.send(pickle.dumps([-1]))
                conn.close()
                break
            elif which_game == 2:  #### GUESSNUMBER
                raise NotImplementedError # NOT IMPLEMENTED YET