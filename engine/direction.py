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


class Direction:
    def __init__(self, name, dx, dy):
        self._name = name
        self._dx = int(dx)
        self._dy = int(dy)

    def change_x(self, x):
        return x + self._dx

    def change_y(self, y):
        return y + self._dy

    def inverted(self):
        if self == LEFT:
            return RIGHT
        if self == RIGHT:
            return LEFT
        if self == UP:
            return DOWN
        if self == DOWN:
            return UP
        raise ValueError(f"Cant invert for: {str(self)}")

    def __str__(self):
        return self._name


LEFT = Direction("LEFT", -1, 0)
RIGHT = Direction("RIGHT", 1, 0)
UP = Direction("UP", 0, 1)
DOWN = Direction("DOWN", 0, -1)
ACT = Direction("ACT", 0, 0)
STOP = Direction("STOP", 0, 0)


if __name__ == "__main__":
    raise RuntimeError("This module is not designed to be ran from CLI")
