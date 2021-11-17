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

import math

from engine.point import Point


class GameBoard:
    def __init__(self, supported_elements, message):
        message = message.replace("board=", "")
        self._elements = self.__init_elements_array(supported_elements, message)
        self._len = len(self._elements)
        self._size = int(math.sqrt(self._len))

    @staticmethod
    def __init_elements_array(supported_elements, message):
        _elements = []
        for next_element in message:
            if next_element not in supported_elements:
                raise ValueError(f"invalid element: {str(next_element)}")

            _elements.append(next_element)
        return _elements

    @property
    def size(self):
        return self._size

    def get_at(self, pt):
        if not pt.is_valid(self._size):
            raise ValueError("invalid point: " + str(pt))
        return self._elements[self.__point_to_index(pt)]

    def find(self, *wanted):
        _points = set()
        for i, e in enumerate(self._elements):
            if e in wanted:
                _points.add(self.__index_to_point(i))
        return sorted(_points)

    def find_first(self, *wanted):
        for i, e in enumerate(self._elements):
            if e in wanted:
                return self.__index_to_point(i)
        return None

    def is_at(self, pt, *wanted):
        return pt.is_valid(self._size) and self.get_at(pt) in wanted

    def find_near(self, pt):
        _elements = []

        right = Point(pt.x + 1, pt.y)
        if right.is_valid(self._size):
            _elements.append(self.get_at(right))
        left = Point(pt.x - 1, pt.y)
        if left.is_valid(self._size):
            _elements.append(self.get_at(left))
        up = Point(pt.x, pt.y + 1)
        if up.is_valid(self._size):
            _elements.append(self.get_at(up))
        down = Point(pt.x, pt.y - 1)
        if down.is_valid(self._size):
            _elements.append(self.get_at(down))

        return _elements

    def count_near(self, pt, *wanted):
        return len(set(self.find_near(pt)) & set(wanted))

    def is_near(self, pt, *wanted):
        for el in wanted:
            if self.count_near(pt, el) != 0:
                return True
        return False

    def __point_to_index(self, pt):
        return (self._size - 1 - pt.y) * self._size + pt.x

    def __index_to_point(self, index):
        x = index % self._size
        y = math.ceil(self._size - 1 - index / self._size)
        return Point(x, y)

    def __str__(self):
        _str = ""
        for y in range(self._size - 1, -1, -1):
            for x in range(self._size):
                index = self.__point_to_index(Point(x, y))
                _str += self._elements[index]
            _str += "\n"
        return _str


if __name__ == "__main__":
    raise RuntimeError("This module is not designed to be ran from CLI")
