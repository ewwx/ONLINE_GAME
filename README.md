[![Build Status](https://travis-ci.com/ewwx/ONLINE_GAME.svg?branch=master)](https://travis-ci.com/ewwx/ONLINE_GAME) [![codecov](https://codecov.io/gh/ewwx/ONLINE_GAME/branch/master/graph/badge.svg)](https://codecov.io/gh/ewwx/ONLINE_GAME)

# ONLINE_GAME

## Getting Started
It is game platform, which include:
* TicTacToe game
  * for one player 
  * for two player
* GuessNumber
Diplayed instructers on the client side:
```
insert your name: 
TicTacToe [1] or Guess Number [2]:
```
if 1 is typed:
```
Singleplayer [1] or Multiplayer [2]:
```
For 2 - Multiplayer version, there is choise of working as a server ar a client, so there are following questions:
```
Do you want work as a server - 1 or as a client - 2:
```
In both situations HOST IP and POST must be typed. So two players, who want to play together must give the same HOST and PORT. When no input is provided (only enter is pressed) the following values are set: 
```
HOST = 'localhost'
PORT = 50008
```
The HOST and PORT must be typed firstly by client, who choose to work as the server.

### Prerequisites
To run this game you need to have Python 3.6 installed

### Installing

Firstly download all files. To run game platform you need to run server first.

```
python server.py
```

And then run client

```
python client.py
```
For TicTacToe game for two players running server is not necessary, but it is recommended. 


## Running the tests

Test are writen with using pytest. If you do not have pytest library just download it with pip.

```
pip install -U pytest
```
and then run the test, for example just like that:

```
pytest TestTicTacToe.py
```

## Authors

* **Ewa Gierlach** - - [ewwx](https://github.com/ewwx)
* **Christian Riva** - - [chririva](https://github.com/chririva)



