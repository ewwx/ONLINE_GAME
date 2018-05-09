import pytest
from TicTacToe import TicTacToe


def test_right_name1():
    game = TicTacToe()
    name = 'Bob'
    game.set_name_player1(name)
    assert name == game.get_name_player1()


def test_right_name2():
    game = TicTacToe()
    name = 'Bob'
    game.set_name_player2(name)
    assert name == game.get_name_player2()

def test_is_free():
    game = TicTacToe()
    result = game.is_free(1)
    ex_result = True
    assert result == ex_result

def test_is_free1():
    game = TicTacToe()
    game.put_choice(2, 4)
    result = game.is_free(4)
    ex_result = False
    assert result == ex_result

def test_symbol1():
    game = TicTacToe()
    assert game.set_symbol1('X') == True


def test_symbol2():
    game = TicTacToe()
    assert game.set_symbol2('O') == True


def test_get_next1():
    game = TicTacToe()
    assert game.get_next() == 1


def test_get_next2():
    game = TicTacToe()
    game.put_choice(1, 100)
    assert game.get_next() == 1


def test_get_next3():
    game = TicTacToe()
    game.put_choice(2, 1)
    assert game.get_next() == 1


def test_get_next4():
    game = TicTacToe()
    game.put_choice(1, 8)
    assert game.get_next() == 2


def test_game1():
    game = TicTacToe()
    game.put_choice(1, 1)
    game.put_choice(2, 2)
    game.put_choice(1, 5)
    game.put_choice(2, 7)
    game.put_choice(1, 9)
    game.put_choice(2, 4)
    assert game.status_of_the_match() == 1


def test_game2():
    game = TicTacToe()
    game.put_choice(1, 1)
    game.put_choice(1, 2)
    game.put_choice(1, 3)
    assert game.status_of_the_match() == 1


def test_game3():
    game = TicTacToe()
    game.put_choice(2, 1)
    game.put_choice(2, 4)
    game.put_choice(1, 10)
    game.put_choice(1, 3)
    game.put_choice(2, 7)
    assert game.status_of_the_match() == 2


def test_game4():
    game = TicTacToe()
    game.put_choice(2, 2)
    game.put_choice(2, 6)
    game.put_choice(2, 9)
    game.put_choice(2, 7)
    game.put_choice(1, 8)
    game.put_choice(1, 5)
    game.put_choice(1, 4)
    game.put_choice(1, 3)
    game.put_choice(1, 1)
    assert game.status_of_the_match() == 3


def test_game4():
    game = TicTacToe()
    game.put_choice(2, 2)
    game.put_choice(2, 6)
    game.put_choice(2, 9)
    game.put_choice(2, 7)
    assert game.status_of_the_match() == 0