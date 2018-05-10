import pytest
from mock import patch
from GuessNumber import GuessNumber


def test_right_name1():
    game = GuessNumber()
    name = 'Bob'
    game.set_name(name)
    assert name == game.name


def test_getting_input1():
    game = GuessNumber()
    with pytest.raises(IOError) as e_info:
        game.getting_input("ff")


def test_getting_input2():
    game = GuessNumber()
    inp = 8
    game.getting_input(inp)
    assert game.in_num == inp and game.quit is False


def test_getting_input3():
    game = GuessNumber()
    inp = "quit"
    game.getting_input(inp)
    assert game.quit is True


def test_getting_input_s():
    game = GuessNumber()
    inp = "quit"
    game.getting_input(inp)
    assert game.quit is True


def test_compare1():
    game = GuessNumber()
    game.getting_input(game.random_number+1)
    res = game.compare()
    assert res == 1


def test_compare2():
    game = GuessNumber()
    game.getting_input(game.random_number-1)
    res = game.compare()
    assert res == -1


def test_compare3():
    game = GuessNumber()
    game.getting_input(game.random_number)
    res = game.compare()
    assert res == 0

## I have error while executing this, I don't understand why
'''
def test_play():
    game = GuessNumber()
    ex_random = game.random_number
    @patch('mod.__get_input', return_value=str(ex_random))
    def run(mock):
        return game.play()
    message = run()
    ex_message = "You guessed in 1 guesses!"
    assert message == ex_message
'''