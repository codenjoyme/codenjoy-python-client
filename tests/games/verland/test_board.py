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

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from unittest import TestCase

from engine.point import Point
from games.verland.board import Board
from games.verland.element import elements


class TestBoard(TestCase):
    def test_get_at_invalid_point(self):
        board = Board("☼☼☼" + "☼☼☼" + "☼☼☼")
        self.assertEqual(elements.get('PATHLESS'), board.get_at(Point(-1, -1)))

    def test_find_hero(self):
        board = Board("☼♥☼" + "☼☼☼" + "☼☼☼")
        self.assertEqual(Point(1, 2), board.find_hero())

        board = Board("☼☼☼" + "☼♥☼" + "☼☼☼")
        self.assertEqual(Point(1, 1), board.find_hero())

        board = Board("☼☼☼" + "☼☼☼" + "☼♥☼")
        self.assertEqual(Point(1, 0), board.find_hero())

        board = Board("☼☼♥" + "☼☼☼" + "☼☼☼")
        self.assertEqual(Point(2, 2), board.find_hero())

    def test_find_hero_no_result(self):
        board = Board("☼☼☼" + "☼☼☼" + "☼☼☼")
        self.assertRaises(ValueError, lambda: board.find_hero())

    def test_is_game_over(self):
        board = Board("☼☼☼" + "☼☼♥" + "☼☼☼")
        self.assertEqual(False, board.is_game_over())

        board = Board("☼☼☼" + "X☼☼" + "☼☼☼")
        self.assertEqual(True, board.is_game_over())

    def test_find_other_heroes(self):
        board = Board("☼Y☼" + "☼♠☼" + "☼☼☼")
        self.assertEqual([Point(1, 1), Point(1, 2)], board.find_other_heroes())

    def test_find_enemy_heroes(self):
        board = Board("☼Z☼" + "☼♣☼" + "☼☼☼")
        self.assertEqual([Point(1, 1), Point(1, 2)], board.find_enemy_heroes())

    def test_find_walls(self):
        board = Board("***" + "☼**" + "☼**")
        self.assertEqual([Point(0, 0), Point(0, 1)], board.find_walls())

    def test_count_contagions(self):
        board = Board("***" + "***" + "8**")
        self.assertEqual(8, board.count_contagions(Point(0, 0)))

    def test_report(self):
        board = Board("☼☼☼☼☼☼☼☼☼" +
                      "☼1 Y   y☼" +
                      "☼*2  x  ☼" +
                      "☼o 3 ♠ +☼" +
                      "☼♥  4   ☼" +
                      "☼   Z  ♣☼" +
                      "☼z  5678☼" +
                      "☼  !  X ☼" +
                      "☼☼☼☼☼☼☼☼☼")
        self.assertEqual("☼☼☼☼☼☼☼☼☼\n" +
                         "☼1 Y   y☼\n" +
                         "☼*2  x  ☼\n" +
                         "☼o 3 ♠ +☼\n" +
                         "☼♥  4   ☼\n" +
                         "☼   Z  ♣☼\n" +
                         "☼z  5678☼\n" +
                         "☼  !  X ☼\n" +
                         "☼☼☼☼☼☼☼☼☼\n" +
                         "\nHero at: [1,4]" +
                         "\nOther heroes at: [[3,7], [5,5]]" +
                         "\nEnemy heroes at: [[4,3], [7,3]]" +
                         "\nOther stuff at: [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7], [0,8], [1,0], "
                         "[1,5], [1,"
                         "6], [1,8], [2,0], [2,8], " +
                         "[3,0], [3,8], [4,0], [4,8], [5,0], [5,8], [6,0], [6,8], [7,0], [7,8], [8,0], [8,1], [8,2], "
                         "[8,3], [8,"
                         "4], [8,5], [8,6], " +
                         "[8,7], [8,8]]", board.__str__())
