"""
    Garfield Maitland
    CS 5001
    11/28/2023
    Final Project - test_mastermind_game.py
"""

from Game import MasterMind


Game = MasterMind()


def test_secret_code():
    """
    Function: test_secret_code()
        A function that tests the secret_code inputted into the program

    Parameters:
        None

    Returns:
        None

    Defense:
        None
    """
    assert len(Game.secret_code) == 4
    assert len(set(Game.secret_code)) == 4
    for i in Game.secret_code:
        assert i in Game.colors


def test_feedback():
    """
    Function: test_feedback()
        Records the secret_code and tests it against the equivalence values

    Parameters:
        None

    Returns:
        None

    Defense:
        None
    """
    Game.secret_code = ["red", "blue", "green", "yellow"]
    assert Game.feedback(["red", "blue", "green", "yellow"]) == {"Bulls": 4, "Cows": 0}
    assert Game.feedback(["red", "black", "green", "yellow"]) == {"Bulls": 3, "Cows": 0}
    assert Game.feedback(["blue", "red", "green", "yellow"]) == {"Bulls": 2, "Cows": 2}
    assert Game.feedback(["blue", "red", "green", "yellow"]) == {"Bulls": 2, "Cows": 2}


if __name__ == "__main__":
    test_secret_code()
    test_feedback()
    print("All tests passed")
