import socket, pickle


class GuessNumberConnection:
    HOST = 'localhost'
    PORT = 50007
    name = "guessName"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, HOST, PORT):
        self.HOST=HOST
        self.PORT=PORT
    def connect(self):
        self.s.connect(('localhost', 50007))
        while 1:
            data = self.s.recv(4096)
            if data:
                data_received = pickle.loads(data)
                if data_received==1:
                    return 1
                return 0
    def close_connection(self):
        self.s.send(pickle.dumps([-1]))
        #data_received = pickle.loads(self.s.recv(4096))
        self.s.close()

    def initial_settings(self,number_of_player,my_name,which_game):
        data_to_send = ([1,number_of_player,my_name,which_game])
        arr = pickle.dumps(data_to_send)
        self.s.send(arr)

    def give_input(self, taken_inp):
        data_to_send = ([2, taken_inp])
        arr = pickle.dumps(data_to_send)
        self.s.send(arr)
        print("Sent:",data_to_send)
        #data_received = pickle.loads(self.s.recv(4096))
        #print(data_received)



    def get_response(self):
        data_received = pickle.loads(self.s.recv(4096))
        print("Response:",data_received)
        return data_received

    def status_of_the_match(self):
        self.s.send(pickle.dumps([4]))
        data_received = pickle.loads(self.s.recv(4096))
        return data_received[1]
