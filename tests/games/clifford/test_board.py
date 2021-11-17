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
from games.clifford.board import Board
from games.clifford.element import elements


class TestBoard(TestCase):
    def test_is_game_over(self):
        board = Board("#####►###");
        self.assertEqual(False, board.is_game_over())

        board = Board("###O#####");
        self.assertEqual(True, board.is_game_over())
        
        board = Board("###o#####");
        self.assertEqual(True, board.is_game_over())

    def test_find_hero(self):
        board = Board("O########")
        self.assertEqual(Point(0, 2), board.find_hero())
                       
        board = Board("###A#####")
        self.assertEqual(Point(0, 1), board.find_hero())
        
        board = Board("####◄####")
        self.assertEqual(Point(1, 1), board.find_hero())
        
        board = Board("#####►###")
        self.assertEqual(Point(2, 1), board.find_hero())
        
        board = Board("######U##")
        self.assertEqual(Point(0, 0), board.find_hero())
                
        board = Board("########I")
        self.assertEqual(Point(2, 0), board.find_hero())
                      
        board = Board("########E")
        self.assertEqual(Point(2, 0), board.find_hero())
        
        board = Board("EO A◄►UI ");
        self.assertEqual(Point(0, 0), board.find_hero())

    def test_find_hero_mask(self):
        board = Board("o########")
        self.assertEqual(Point(0, 2), board.find_hero())
                       
        board = Board("###a#####")
        self.assertEqual(Point(0, 1), board.find_hero())
        
        board = Board("####h####")
        self.assertEqual(Point(1, 1), board.find_hero())
        
        board = Board("#####w###")
        self.assertEqual(Point(2, 1), board.find_hero())
        
        board = Board("######u##")
        self.assertEqual(Point(0, 0), board.find_hero())
                        
        board = Board("########i")
        self.assertEqual(Point(2, 0), board.find_hero())
                
        board = Board("########e")
        self.assertEqual(Point(2, 0), board.find_hero())
                
        board = Board("eo awhui ")
        self.assertEqual(Point(0, 0), board.find_hero())

    def test_find_hero_no_result(self):
        board = Board("#########")
        self.assertRaises(ValueError, lambda: board.find_hero())

    def test_find_other_heroes(self):
        board = Board("C» D« KJF")
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(0, 2),
             Point(1, 0), Point(1, 1), Point(1, 2),
             Point(2, 0)], board.find_other_heroes())

        board = Board("cz dZ kjf")
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(0, 2),
             Point(1, 0), Point(1, 1), Point(1, 2),
             Point(2, 0)], board.find_other_heroes())

    def test_find_enemy_heroes(self):
        board = Board("LP NQ RTV")
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(0, 2),
             Point(1, 0), Point(1, 1), Point(1, 2),
             Point(2, 0)],  board.find_enemy_heroes())

        board = Board("lp nq rtv")
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(0, 2),
             Point(1, 0), Point(1, 1), Point(1, 2),
             Point(2, 0)],  board.find_enemy_heroes())

    def test_find_robbers(self):
        board = Board("X) xY (y ")
        self.assertEqual(
            [Point(0, 0), Point(0, 1), Point(0, 2),
             Point(1, 0), Point(1, 1), Point(1, 2)], board.find_robbers())

    def test_find_barriers(self):
        board = Board("  #  ☼   ")
        self.assertEqual([Point(2, 1), Point(2, 2)], board.find_barriers())

    def test_find_pits(self):
        board = Board("1234**###")
        self.assertEqual([Point(0, 1), Point(0, 2), Point(1, 1),
                          Point(1, 2), Point(2, 1), Point(2, 2)], board.find_pits())

    def test_find_clues(self):
        board = Board("##$##&##@")
        self.assertEqual([Point(2, 0), Point(2, 1), Point(2, 2)], board.find_clues())

    def test_find_backways(self):
        board = Board("##W######")
        self.assertEqual([Point(2, 2)], board.find_backways())

    def test_find_potions(self):
        board = Board("##m######")
        self.assertEqual([Point(2, 2)], board.find_potions())

    def test_find_doors(self):
        board = Board("gsbGSB###")
        self.assertEqual([Point(0, 1), Point(0, 2), Point(1, 1),
                          Point(1, 2), Point(2, 1), Point(2, 2)], board.find_doors())

    def test_find_keys(self):
        board = Board("+-!######")
        self.assertEqual([Point(0, 2), Point(1, 2), Point(2, 2)], board.find_keys())

    def test_report(self):
        board = Board("board=" +
                      "☼☼☼☼☼☼☼☼☼" +
                      "☼ ►*## $☼" +
                      "☼ H pq -☼" +
                      "☼ H  1 G☼" +
                      "☼m   &  ☼" +
                      "☼ + ~~~ ☼" +
                      "☼Z3 S   ☼" +
                      "☼ @@  X ☼" +
                      "☼☼☼☼☼☼☼☼☼")
        self.assertEqual("☼☼☼☼☼☼☼☼☼\n" +
                         "☼ ►*## $☼\n" +
                         "☼ H pq -☼\n" +
                         "☼ H  1 G☼\n" +
                         "☼m   &  ☼\n" +
                         "☼ + ~~~ ☼\n" +
                         "☼Z3 S   ☼\n" +
                         "☼ @@  X ☼\n" +
                         "☼☼☼☼☼☼☼☼☼\n" +
                         "\n" +
                         "Hero at: [2,7]\n"
                         "Other heroes at: [[1,2]]\n"
                         "Enemy heroes at: [[4,6], [5,6]]\n"
                         "Robbers at: [[6,1]]\n"
                         "Mask potions at: [[1,4]]\n"
                         "Keys at: [[2,3], [7,6]]", board.__str__())
