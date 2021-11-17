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

import os.path
import sys
from unittest import TestCase

from engine import direction

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


class TestDirection(TestCase):
    def test_value(self):
        self.assertEqual(0, direction.LEFT.value)
        self.assertEqual(1, direction.RIGHT.value)
        self.assertEqual(2, direction.UP.value)
        self.assertEqual(3, direction.DOWN.value)
        self.assertEqual(4, direction.ACT.value)
        self.assertEqual(5, direction.STOP.value)

    def test_change_x(self):
        self.assertEqual(0, direction.LEFT.change_x(1))
        self.assertEqual(2, direction.RIGHT.change_x(1))
        self.assertEqual(1, direction.UP.change_x(1))
        self.assertEqual(1, direction.DOWN.change_x(1))

    def test_change_y(self):
        self.assertEqual(1, direction.LEFT.change_y(1))
        self.assertEqual(1, direction.RIGHT.change_y(1))
        self.assertEqual(2, direction.UP.change_y(1))
        self.assertEqual(0, direction.DOWN.change_y(1))

    def test_inverted(self):
        self.assertEqual(direction.RIGHT, direction.LEFT.inverted())
        self.assertEqual(direction.LEFT, direction.RIGHT.inverted())
        self.assertEqual(direction.DOWN, direction.UP.inverted())
        self.assertEqual(direction.UP, direction.DOWN.inverted())

    def test_invalid_inverted(self):
        with self.assertRaises(ValueError):
            direction.ACT.inverted()
        with self.assertRaises(ValueError):
            direction.STOP.inverted()
