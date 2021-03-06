#!/usr/bin/env python3

###
# #%L
# Codenjoy - it's a dojo-like platform from developers to developers.
# %%
# Copyright (C) 2012 - 2022 Codenjoy
# %%
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/gpl-3.0.html>.
# #L%
###

import os.path
import sys
from unittest import TestCase

from engine.game_board import GameBoard
from engine.point import Point

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


class TestGameBoard(TestCase):
    def test_empty_message(self):
        board = GameBoard(["a", "b", "c"], "")
        self.assertEqual("", str(board))

    def test_empty_supported_elements(self):
        with self.assertRaises(ValueError):
            GameBoard([], "aaa" + "bbb" + "ccc")

    def test_valid_message_and_supported_elements(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual("aaa\nbbb\nccc\n", str(board))

    def test_erase_message_prefix(self):
        board = GameBoard(["a", "b", "c"], "board=" + "aaa" + "bbb" + "ccc")
        self.assertEqual("aaa\nbbb\nccc\n", str(board))

    def test_message_with_unsupported_elements(self):
        with self.assertRaises(ValueError):
            GameBoard(["a", "b", "c"], "ab8c")

    def test_get_size(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual(3, board.size)

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

    def test_get_at_invalid_point(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        with self.assertRaises(ValueError):
            board.get_at(Point(10, 10))

    def test_find(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertEqual(
            [Point(0, 2), Point(1, 2), Point(2, 2)],
            board.find("a")
        )
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 0), Point(2, 1)],
            board.find("b", "c")
        )

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
        self.assertIsNone(board.find_first("d"))

    def test_is_at(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertTrue(board.is_at(Point(1, 2), "a"))
        self.assertFalse(board.is_at(Point(1, 2), "b"))
        self.assertFalse(board.is_at(Point(1, 2), "c"))

    def test_is_at_invalid_point(self):
        board = GameBoard(["a", "b", "c"], "aaa" + "bbb" + "ccc")
        self.assertFalse(board.is_at(Point(10, 10), "b"))

    def test_find_near(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertEqual(["f", "d", "b", "h"], board.find_near(Point(1, 1)))

    def test_find_near_invalid_point(self):
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
        self.assertFalse(board.is_near(Point(1, 1), "a"))
        self.assertTrue(board.is_near(Point(1, 1), "b"))
        self.assertTrue(board.is_near(Point(1, 1), "c", "d"))

    def test_is_near_invalid_point(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertFalse(board.is_near(Point(-1, -1), "a"))

    def test_is_near_not_existed_element(self):
        board = GameBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"], "abc" + "def" + "ghi")
        self.assertFalse(board.is_near(Point(1, 1), "r"))
        self.assertFalse(board.is_near(Point(1, 1), "x", "y", "z"))
