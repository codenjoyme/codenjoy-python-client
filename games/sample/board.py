#!/usr/bin/env python3

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

from engine.game_board import GameBoard
from engine.point import step_left, step_right, step_up, step_down
from games.sample.element import elements


class Board:

    def __init__(self, message):
        self._board = GameBoard(elements.values(), message)

    def is_game_over(self):
        return self._board.find_first(elements.get('DEAD_HERO')) is not None

    def __str__(self):
        return self._board.__str__()


if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
