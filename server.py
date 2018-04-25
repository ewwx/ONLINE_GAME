
import socket, pickle
from TicTacToe import TicTacToe
from GuessNumber import GuessNumber

HOST = 'localhost'
PORT = 50007
SERVER_STATUS = 0

while SERVER_STATUS == 0:
    print("SERVER IS ONLINE")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            print("RECEIVED: ", repr(data_arr))
            if data_arr[0] == 1:
                #GAME INITIALIZATION:
                if data_arr[3] == 1:
                    print("STARTING TIC TAC TOE")
                    game = TicTacToe()
                    game.set_name_player1(data_arr[2])
                    if data_arr[1] == 1:
                        SERVER_STATUS = 1
                    else:
                        SERVER_STATUS = 2
                    break
                elif data_arr[3] == 2:
                    print("STARTING GUESS NUMBER")
                    game = GuessNumber()
                    if data_arr[1] == 1:
                        SERVER_STATUS = 1
                    else:
                        SERVER_STATUS = 2
                    break
    print("SERVER_STATUS: ",SERVER_STATUS)
    while SERVER_STATUS == 2:
        raise NotImplementedError #NOT IMPLEMENTED YET
    while SERVER_STATUS == 1:
        while 1:
            data = conn.recv(4096)
            if data:
                # conn.send(data)
                data_arr = pickle.loads(data)
                print("RECEIVED: ", repr(data_arr))
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
                elif data_arr[0] == 5:
                    #get next
                    conn.send(pickle.dumps([5, game.get_next()]))
                elif data_arr[0] == 6:
                    #is free
                    conn.send(pickle.dumps([6, game.is_free(data_arr[1])]))
                elif data_arr[0] == 7:
                    #computer turn
                    conn.send(pickle.dumps([7, game.computer_turn()]))
                elif data_arr[0] == -1:
                    #CLOSE CONNECTION
                    print("CONNECTION CLOSED")
                    SERVER_STATUS = 0
                    conn.send(pickle.dumps([-1]))
                    conn.close()
                    break
