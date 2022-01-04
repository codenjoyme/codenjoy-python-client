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

from engine import direction
from engine.game_solver import GameSolver
from games.sample.board import Board


class Solver(GameSolver):

    def answer(self, message):
        board = Board(message)
        print("Board \n" + board.__str__())
        action = self.__next_action()
        print("\nAnswer: " + action.__str__())
        print("-------------------------------------------------------------")
        return action.__str__()

    def __next_action(self):
        # TODO: write your code here
        return direction.ACT


if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
