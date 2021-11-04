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
from games.mollymage.board import Board
from games.mollymage.element import elements


class TestBoard(TestCase):
    def test_get_at_invalid_point(self):
        board = Board("###" + "###" + "###")
        self.assertEqual(elements.get('WALL'), board.get_at(Point(-1, -1)))

    def test_find_hero(self):
        board = Board("#☺#" + "###" + "###")
        self.assertEqual(Point(1, 2), board.find_hero())

        board = Board("###" + "#☻#" + "###")
        self.assertEqual(Point(1, 1), board.find_hero())

        board = Board("###" + "###" + "#Ѡ#")
        self.assertEqual(Point(1, 0), board.find_hero())

        board = Board("Ѡ☺☻" + "###" + "###")
        self.assertEqual(Point(0, 2), board.find_hero())

    def test_find_hero_no_result(self):
        board = Board("###" + "###" + "###")
        self.assertRaises(ValueError, lambda: board.find_hero())

    def test_is_game_over(self):
        board = Board("###" + "##☺" + "###")
        self.assertEqual(False, board.is_game_over())

        board = Board("###" + "Ѡ##" + "###")
        self.assertEqual(True, board.is_game_over())

    def test_find_other_heroes(self):
        board = Board("#♥#" + "#♠#" + "#♣#")
        self.assertEqual([Point(1, 0), Point(1, 1), Point(1, 2)], board.find_other_heroes())

    def test_find_enemy_heroes(self):
        board = Board("#ö#" + "#Ö#" + "#ø#")
        self.assertEqual([Point(1, 0), Point(1, 1), Point(1, 2)], board.find_enemy_heroes())

    def test_find_barriers(self):
        board = Board("☼&#" + "123" + "♥♠♣")
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(0, 2),
             Point(1, 0), Point(1, 1), Point(1, 2),
             Point(2, 0), Point(2, 1), Point(2, 2)],
            board.find_barriers())

    def test_find_walls(self):
        board = Board("###" + "☼##" + "☼##")
        self.assertEqual([Point(0, 0), Point(0, 1)], board.find_walls())

    def test_find_ghosts(self):
        board = Board("##&" + "##&" + "###")
        self.assertEqual([Point(2, 1), Point(2, 2)], board.find_ghosts())

    def test_find_treasure_boxes(self):
        board = Board("҉#҉" + "҉҉҉" + "҉#҉")
        self.assertEqual([Point(1, 0), Point(1, 2)], board.find_treasure_boxes())

    def test_find_potions(self):
        board = Board("123" + "45#" + "☻♠#")
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 0), Point(1, 1), Point(1, 2), Point(2, 2)],
            board.find_potions())

    def test_find_blasts(self):
        board = Board("###" + "###" + "##҉")
        self.assertEqual([Point(2, 0)], board.find_blasts())

    def test_find_perks(self):
        board = Board("#cr" + "#i+" + "#TA")
        self.assertEqual(
            [Point(1, 0), Point(1, 1), Point(1, 2), Point(2, 0), Point(2, 1), Point(2, 2)],
            board.find_perks())

    def test_report(self):
        board = Board("board=" +
                      "☼☼☼☼☼☼☼☼☼" +
                      "☼1 ♣   ♠☼" +
                      "☼#2  &  ☼" +
                      "☼# 3 ♣ ♠☼" +
                      "☼☺  4   ☼" +
                      "☼   ö H☻☼" +
                      "☼x H ҉҉҉☼" +
                      "☼& &    ☼" +
                      "☼☼☼☼☼☼☼☼☼")
        self.assertEqual("☼☼☼☼☼☼☼☼☼\n" +
                          "☼1 ♣   ♠☼\n" +
                          "☼#2  &  ☼\n" +
                          "☼# 3 ♣ ♠☼\n" +
                          "☼☺  4   ☼\n" +
                          "☼   ö H☻☼\n" +
                          "☼x H ҉҉҉☼\n" +
                          "☼& &    ☼\n" +
                          "☼☼☼☼☼☼☼☼☼\n" +
                          "\n" +
                          "Hero at: [1,4]\n" +
                          "Other heroes at: [[3,7], [5,5], [7,5], [7,7]]\n" +
                          "Enemy heroes at: [[4,3]]\n" +
                          "Ghosts at: [[1,1], [3,1], [5,6]]\n" +
                          "Potions at: [[1,7], [2,6], [3,5], [4,4], [7,3], [7,5], [7,7]]\n" +
                          "Blasts at: [[5,2], [6,2], [7,2]]\n" +
                          "Expected blasts at: [[2,7]]", board.__str__())
