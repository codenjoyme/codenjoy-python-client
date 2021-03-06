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

from engine.game_board import GameBoard
from engine.point import Point

from games.verland.element import elements


class Board:
    def __init__(self, message):
        self._board = GameBoard(elements.values(), message)

    def is_game_over(self):
        return self._board.find_first(elements.get("HERO_DEAD")) is not None

    def get_at(self, pt):
        if not pt.is_valid(self._board.size):
            return elements.get('PATHLESS')
        return self._board.get_at(pt, pt)

    def find_hero(self):
        points = self._board.find(
            elements.get("HERO_DEAD"),
            elements.get("HERO"),
        )

        if not points:
            raise ValueError("Hero element has not been found")
        return points[0]

    def find_other_heroes(self):
        return self._board.find(
            elements.get("OTHER_HERO_DEAD"),
            elements.get("OTHER_HERO"),
        )

    def find_enemy_heroes(self):
        return self._board.find(
            elements.get("ENEMY_HERO_DEAD"),
            elements.get("ENEMY_HERO"),
        )

    def find_other_stuff(self):
        return self._board.find(
            elements.get("INFECTION"),
            elements.get("HIDDEN"),
            elements.get("PATHLESS"),
        )

    def find_walls(self):
        return self._board.find(elements.get("PATHLESS"))

    # public
    # int
    # countContagions(Point
    # point) {
    # return is (point, infectionMarkers()) ? getAt(point).value(): 0;
    # }
    def count_contagions(self, pt):
        return int(self._board.get_at(pt)) if self._board.is_at(pt,
                                                                elements.get("CLEAR"),
                                                                elements.get("CONTAGION_ONE"),
                                                                elements.get("CONTAGION_TWO"),
                                                                elements.get("CONTAGION_THREE"),
                                                                elements.get("CONTAGION_FOUR"),
                                                                elements.get("CONTAGION_FIVE"),
                                                                elements.get("CONTAGION_SIX"),
                                                                elements.get("CONTAGION_SEVEN"),
                                                                elements.get("CONTAGION_EIGHT"),
                                                                ) else 0

    def __str__(self):
        return (
                self._board.__str__()
                + "\nHero at: "
                + repr(self.find_hero())
                + "\nOther heroes at: "
                + repr(self.find_other_heroes())
                + "\nEnemy heroes at: "
                + repr(self.find_enemy_heroes())
                + "\nOther stuff at: "
                + repr(self.find_other_stuff())
        )


if __name__ == "__main__":
    raise RuntimeError("This module is not intended to be ran from CLI")
