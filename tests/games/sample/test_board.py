#!/usr/bin/env python3

###
# #%L
# Codenjoy - it's a dojo-like platform from developers to developers.
# %%
# Copyright (C) 2021 Codenjoy
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

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from unittest import TestCase

from engine.point import Point
from games.sample.board import Board
from games.sample.element import elements


class TestBoard(TestCase):
    def test_get_at_invalid_point(self):
        board = Board("☼☼☼" + "☼☼☼" + "☼☼☼")
        self.assertEqual(elements.get('WALL'), board.get_at(Point(-1, -1)))

    def test_find_hero(self):
        board = Board("☼☺☼" + "☼☼☼" + "☼☼☼")
        self.assertEqual(Point(1, 2), board.find_hero())

        board = Board("☼☼☼" + "☼☺☼" + "☼☼☼")
        self.assertEqual(Point(1, 1), board.find_hero())

        board = Board("☼☼☼" + "☼☼☼" + "☼X☼")
        self.assertEqual(Point(1, 0), board.find_hero())

        board = Board("X☺☻" + "☼☼☼" + "☼☼☼")
        self.assertEqual(Point(0, 2), board.find_hero())

    def test_find_hero_no_result(self):
        board = Board("☼☼☼" + "☼☼☼" + "☼☼☼")
        self.assertRaises(ValueError, lambda: board.find_hero())

    def test_is_game_over(self):
        board = Board("☼☼☼" + "☼☼☺" + "☼☼☼")
        self.assertEqual(False, board.is_game_over())

        board = Board("☼☼☼" + "X☼☼" + "☼☼☼")
        self.assertEqual(True, board.is_game_over())

    def test_find_other_heroes(self):
        board = Board("☼☻☼" + "☼Y☼" + "☼☻☼")
        self.assertEqual([Point(1, 0), Point(1, 1), Point(1, 2)], board.find_other_heroes())

    def test_find_barriers(self):
        board = Board("☼☼☼" + "xxx" + "☻☻☻")
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(0, 2),
             Point(1, 0), Point(1, 1), Point(1, 2),
             Point(2, 0), Point(2, 1), Point(2, 2)],
            board.find_barriers())

    def test_find_walls(self):
        board = Board("   " + "☼  " + "☼  ")
        self.assertEqual([Point(0, 0), Point(0, 1)], board.find_walls())

    def test_find_gold(self):
        board = Board("☼☼$" + "☼☼$" + "☼☼☼")
        self.assertEqual([Point(2, 1), Point(2, 2)], board.find_gold())

    def test_find_bombs(self):
        board = Board("☼☼x" + "☼☼x" + "☼☼☼")
        self.assertEqual([Point(2, 1), Point(2, 2)], board.find_bombs())

    def test_report(self):
        board = Board("board=" +
                      "☼☼☼☼☼☼☼☼☼" +
                      "☼ x☺  Y ☼" +
                      "☼  x    ☼" +
                      "☼ $  ☻  ☼" +
                      "☼      x☼" +
                      "☼ ☻     ☼" +
                      "☼       ☼" +
                      "☼ $ ☻ x ☼" +
                      "☼☼☼☼☼☼☼☼☼")
        self.assertEqual("☼☼☼☼☼☼☼☼☼\n"+ #8#
                         "☼ x☺  Y ☼\n"+ #7#
                         "☼  x    ☼\n"+ #6#
                         "☼ $  ☻  ☼\n"+ #5#
                         "☼      x☼\n"+ #4#
                         "☼ ☻     ☼\n"+ #3#
                         "☼       ☼\n"+ #2#
                         "☼ $ ☻ x ☼\n"+ #1#
                         "☼☼☼☼☼☼☼☼☼\n"+ #0#
                         #012345678#
                          "\n" +
                          "Hero at: [3,7]\n" +
                          "Other heroes at: [[2,3], [4,1], [5,5], [6,7]]\n" +
                          "Bombs at: [[2,7], [3,6], [6,1], [7,4]]\n" +
                          "Gold at: [[2,1], [2,5]]", board.__str__())
