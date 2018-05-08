import socket, pickle

class TicTacToeClientConnection:
    HOST = 'localhost'
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, HOST, PORT):
        self.HOST=HOST
        self.PORT=PORT

    def connect(self):
        self.s.connect((self.HOST, self.PORT))
        while 1:
            data = self.s.recv(4096)
            if data:
                data_received = pickle.loads(data)
                if data_received==1:
                    return 1
                return 0
    def close_connection(self):
        self.s.send(pickle.dumps([-1]))
        data_received = pickle.loads(self.s.recv(4096))
        self.s.close()

    def initial_settings(self,number_of_player,my_name,which_game):
        data_to_send = ([1,number_of_player,my_name,which_game])
        arr = pickle.dumps(data_to_send)
        self.s.send(arr)
        #data = self.s.recv(4096)
        #data_received = pickle.loads(data)

    def battlefield_request(self):
        data_to_send = ([2])
        arr = pickle.dumps(data_to_send)
        self.s.send(arr)
        data = self.s.recv(4096)
        data_received = pickle.loads(data)
        return data_received[1]

    def put_choice(self,player,location):
        self.s.send(pickle.dumps([3,player,location]))
        data = self.s.recv(4096)
        data_received = pickle.loads(data)

    def status_of_the_match(self):
        self.s.send(pickle.dumps([4]))
        data_received = pickle.loads(self.s.recv(4096))
        return data_received[1]

    def status_of_the_match2players(self,message):
        self.s.send(pickle.dumps([42,message]))
        data_received = pickle.loads(self.s.recv(4096))
        return data_received[1]

    def get_next(self):
        self.s.send(pickle.dumps([5]))
        data_received = pickle.loads(self.s.recv(4096))
        return data_received[1]

    def is_free(self,choice):
        self.s.send(pickle.dumps([6,choice]))
        data_received = pickle.loads(self.s.recv(4096))
        return data_received[1]

    def computer_turn(self):
        self.s.send(pickle.dumps([7]))
        data_received = pickle.loads(self.s.recv(4096))

