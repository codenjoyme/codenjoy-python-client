import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from unittest import TestCase

from engine.game_board import GameBoard
from engine.point import Point


class TestGameBoard(TestCase):
    def test_empty_message(self):
        board = GameBoard(["a", "b", "c"], "")
        self.assertEqual("", board.__str__())

    def test_empty_supported_elements(self):
        self.assertRaises(ValueError, lambda: GameBoard([], "aaa" + "bbb" + "ccc"))

    def test_valid_message_and_supported_elements(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual("aaa\nbbb\nccc\n", board.__str__())

    def test_erase_message_prefix(self):
        board = GameBoard(["a", "b", "c"], "board=" + "aaa" + "bbb" + "ccc")
        self.assertEqual("aaa\nbbb\nccc\n", board.__str__())

    def test_message_with_unsupported_elements(self):
        self.assertRaises(ValueError, lambda: GameBoard(["a", "b", "c"], "ab8c"))

    def test_get_size(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual(3, board.get_size())

    def test_get_at(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual("c", board.get_at(Point(0, 0)))
        self.assertEqual("c", board.get_at(Point(1, 0)))
        self.assertEqual("c", board.get_at(Point(2, 0)))
        self.assertEqual("b", board.get_at(Point(0, 1)))
        self.assertEqual("b", board.get_at(Point(1, 1)))
        self.assertEqual("b", board.get_at(Point(2, 1)))
        self.assertEqual("a", board.get_at(Point(0, 2)))
        self.assertEqual("a", board.get_at(Point(1, 2)))
        self.assertEqual("a", board.get_at(Point(2, 2)))

    def test_getAt_invalid_point(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertRaises(ValueError, lambda: board.get_at(Point(10, 10)))

    def test_find(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual(
            [Point(0, 2), Point(1, 2), Point(2, 2)],
            board.find("a"))
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 0), Point(2, 1)],
            board.find("b", "c"))

    def test_find_not_existed_element(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual([], board.find("d"))

    def test_find_first(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual(Point(0, 0), board.find_first("c"))
        self.assertEqual(Point(0, 1), board.find_first("b", "c"))
        self.assertEqual(Point(0, 1), board.find_first("c", "b"))

    def test_find_first_not_existed_element(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual(None, board.find_first("d"))

    def test_is_at(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual(True, board.is_at(Point(1, 2), "a"))
        self.assertEqual(False, board.is_at(Point(1, 2), "b"))
        self.assertEqual(False, board.is_at(Point(1, 2), "c"))

    def test_is_at_invalid_point(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual(False, board.is_at(Point(10, 10), "b"))

    def test_findNear(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual(["f", "d", "b", "h"], board.find_near(Point(1, 1)))

    def test_findNear_invalid_point(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual([], board.find_near(Point(-1, -1)))

    def test_count_near(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual(2, board.count_near(Point(1, 1), "a", "b", "c", "d"))

    def test_count_near_invalid_point(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual(0, board.count_near(Point(-1, -1), "a", "b", "c", "d"))

    def test_count_near_not_existed_element(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual(0, board.count_near(Point(1, 1), "r"))
        self.assertEqual(0, board.count_near(Point(1, 1), "x", "y", "z"))

    def test_is_near(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual(False, board.is_near(Point(1, 1), "a"))
        self.assertEqual(True, board.is_near(Point(1, 1), "b"))
        self.assertEqual(True, board.is_near(Point(1, 1), "c", "d"))

    def test_is_near_invalid_point(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual(False, board.is_near(Point(-1, -1), "a"))

    def test_is_near_not_existed_element(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual(False, board.is_near(Point(1, 1), "r"))
        self.assertEqual(False, board.is_near(Point(1, 1), "x", "y", "z"))
