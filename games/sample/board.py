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

    def get_at(self, pt):
        if not pt.is_valid(self._board.size):
            return elements.get('WALL')
        return self._board.get_at(pt)

    def find_hero(self):
        points = self._board.find(
            elements.get('HERO'),
            elements.get('DEAD_HERO'),
        )
        if len(points) == 0:
            raise ValueError("Hero element has not been found")
        return points.__iter__().__next__()

    def is_game_over(self):
        return self._board.find_first(elements.get('DEAD_HERO')) is not None

    def find_other_heroes(self):
        return self._board.find(elements.get('OTHER_HERO'),
                                elements.get('OTHER_DEAD_HERO'))

    def find_bombs(self):
        return self._board.find(elements.get('BOMB'))

    def find_gold(self):
            return self._board.find(elements.get('GOLD'))

    def find_barriers(self):
        points = set()
        points.update(self.find_walls())
        points.update(self.find_bombs())
        points.update(self.find_other_heroes())
        return sorted(points)

    def find_walls(self):
        return self._board.find(elements.get('WALL'))

    def __str__(self):
        return self._board.__str__() + \
               "\nHero at: " + repr(self.find_hero()) + \
               "\nOther heroes at: " + repr(self.find_other_heroes()) + \
               "\nBombs at: " + repr(self.find_bombs()) + \
               "\nGold at: " + repr(self.find_gold())

if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
