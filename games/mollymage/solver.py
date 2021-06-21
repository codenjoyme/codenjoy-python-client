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

from engine.direction import Direction
from games.mollymage.board import Board


class Solver:

    def __init__(self):
        self._direction = None
        self._board = None
        self._last = None
        self._count = 0

    def get(self, board_string):
        self._board = Board(board_string)
        print("Board \n{}".format(self._board.to_string()))
        _command = self.next_step()
        print("Answer: {}".format(_command))
        print("-------------------------------------------------------------")

        return _command

    def next_step(self):
        # make your action
        return Direction('ACT').to_string()


if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
