#! /usr/bin/env python3

###
# #%L
# Codenjoy - it's a dojo-like platform from developers to developers.
# %%
# Copyright (C) 2018 Codenjoy
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

from math import sqrt
from engine.point import Point


class Element:
    def __init__(self, char):
        self._char = char

    def get_char(self):
        return self._char

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __str__(self):
        return self._char


class AbstractBoard:
    def __init__(self, raw_board):
        self._content = raw_board.replace('\n', '')
        self._len = len(self._content)
        self._size = int(sqrt(self._len))

    def get_at(self, x, y):
        return Element(self._content[self._xy2strpos(x, y)])

    def get(self, *elements):
        _points = []
        for x in range(0, self._size):
            for y in range(0, self._size):
                for e in elements:
                    if self.get_at(x, y).get_char() == e.get_char():
                        _points.append(Point(x, y))
        return _points

    def get_first(self, *elements):
        for x in range(0, self._size):
            for y in range(0, self._size):
                for e in elements:
                    if self.get_at(x, y).get_char() == e.get_char():
                        return Point(x, y)
        return None

    def is_at(self, x, y, *elements):
        if Point(x, y).is_bad(self._size):
            return False
        return self.get_at(x, y) in elements

    def get_near(self, x, y):
        _elements = []
        if not Point(x + 1, y).is_bad(self._size):
            _elements.append(self.get_at(x + 1, y))
        if not Point(x - 1, y).is_bad(self._size):
            _elements.append(self.get_at(x - 1, y))
        if not Point(x, y + 1).is_bad(self._size):
            _elements.append(self.get_at(x, y + 1))
        if not Point(x, y - 1).is_bad(self._size):
            _elements.append(self.get_at(x, y - 1))
        return _elements

    def is_near(self, x, y, element):
        return element in self.get_near(x, y)

    def count_near(self, x, y, element):
        count = 0
        for e in self.get_near(x, y):
            if element.get_char() == e.get_char():
                count += 1
        return count

    def _strpos2pt(self, strpos):
        return Point(*self._strpos2xy(strpos))

    def _strpos2xy(self, strpos):
        return strpos % self._size, (self._size - strpos // self._size) - 1

    def _xy2strpos(self, x, y):
        return (self._size - 1 - y) * self._size + x


if __name__ == '__main__':
    raise RuntimeError("This module is not designed to be ran from CLI")
