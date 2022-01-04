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

from engine.point import Point

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


class TestPoint(TestCase):
    def test_valid_points(self):
        self.assertTrue(Point(0, 0).is_valid(10))
        self.assertTrue(Point(5, 5).is_valid(10))
        self.assertTrue(Point(10, 10).is_valid(10))
        self.assertTrue(Point(0, 10).is_valid(10))
        self.assertTrue(Point(10, 0).is_valid(10))

    def test_invalid_points(self):
        self.assertFalse(Point(-1, 10).is_valid(10))
        self.assertFalse(Point(10, -1).is_valid(10))
        self.assertFalse(Point(11, 10).is_valid(10))
        self.assertFalse(Point(10, 11).is_valid(10))
