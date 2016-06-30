import unittest
import lib.moves as moves
from lib.game import Game, MoveError
from lib.point import Point


class GameTests(unittest.TestCase):
    def test_a_valid_game_can_be_created(self):
        # The three A's of testing:
        # Arrange
        game = self.create_default_game()

        # Assert
        self.assertFalse(game.has_won)

    # TODO: TEST WINNING: create a board, set squirrel and nut location, move squirrel to nut, check win.
    # hint: moves.py contains a set of possible moves, write a game.move(moves.DIRECTION) method
    # e.g. game.move(moves.up)
    def test_game_can_be_won_wimpy_impl(self):
        # Arrange
        game = self.create_default_game()

        # act
        game.place_squirrel(2, 3)

        # assert
        self.assertTrue(game.has_won)

    def test_squirrel_cannot_be_placed_in_invalid_location(self):
        # Arrange
        game = self.create_default_game()

        # act
        with self.assertRaises(MoveError):
            game.place_squirrel(9, 3)

    def create_default_game(self):
        game = Game()
        game.place_squirrel(0, 0)
        game.place_nut(2, 3)
        return game

#
#
# def test_thing():
#     x = 7
#     y = 11
#     assert(x > y)



















