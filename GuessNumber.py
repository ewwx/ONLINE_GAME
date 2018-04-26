import numpy as np


class GuessNumber:
    def __init__(self):
        self.random_number = np.random.randint(0, 100, dtype=int)
        self.iter = 0
        self.in_num = -1
        self.quit = False
        self.name = "No name"

    def set_name(self, name):
        self.name = name

    def getting_input(self, m):
        try:
            if "quit" == m.casefold():
                self.quit = True
            else:
                self.quit = False
                self.in_num = int(m)
        except ValueError or TypeError:
            self.quit = False
            print('Wrong value! Put an integer or just type "quit" ')
            self.getting_input(input('Type your guess, or type "quit" to quit\n'))

    def getting_input_s(self, m):
        if "quit" == m.casefold():
            self.quit = True
        else:
            self.quit = False
            self.in_num = int(m)

    def compare(self):
        if self.in_num>self.random_number:
            return 1
        elif self.in_num>self.random_number:
            return -1
        else: return 0

    def play(self, inp):
        print("Welcome! I will take an integer from range of 0 to 100. Try to guess this number!")
        while True:
            self.getting_input(input('Type your guess, or type "quit" to quit\n'))
            if self.quit:
                print('game stopped')
                break
            elif self.in_num > self.random_number:
                self.iter += 1
                print("to high")
            elif self.in_num < self.random_number:
                self.iter += 1
                print("to low")
            else:
                self.iter += 1
                print("You guessed in ", self.iter,  "guesses!")
                break
        return 0


if __name__ == "__main__":
    new_game = GuessNumber()
    new_game.play()


