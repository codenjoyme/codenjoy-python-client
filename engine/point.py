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


class Point:
    def __init__(self, x=0, y=0):
        self._x = int(x)
        self._y = int(y)

    @property
    def key(self):
        return self._x, self._y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def is_valid(self, board_size):
        return (0 <= self._x <= board_size) and (0 <= self._y <= board_size)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __gt__(self, other):
        return (self._x, self._y) > (other.x, other.y)

    def __eq__(self, other_point):
        return self.key == other_point.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"[{self._x},{self._y}]"


def step_right(pt):
    return Point(pt.x + 1, pt.y)


def step_left(pt):
    return Point(pt.x - 1, pt.y)


def step_up(pt):
    return Point(pt.x, pt.y + 1)


def step_down(pt):
    return Point(pt.x, pt.y - 1)


if __name__ == "__main__":
    raise RuntimeError("This module is not expected to be ran from CLI")
