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
from games.mollymage.element import elements


class Board:
    BLAST_RANGE = 3

    def __init__(self, message):
        self._board = GameBoard(elements.values(), message)

    def get_at(self, pt):
        if not pt.is_valid(self._board.get_size()):
            return elements.get('WALL')
        return self._board.get_at(pt)

    def find_hero(self):
        points = self._board.find(
            elements.get('HERO'),
            elements.get('POTION_HERO'),
            elements.get('DEAD_HERO'),
        )
        if len(points) == 0:
            raise ValueError("hero element has not been found")
        return points.__iter__().__next__()

    def is_game_over(self):
        return self._board.find_first(elements.get('DEAD_HERO')) is not None

    def find_other_heroes(self):
        return self._board.find(elements.get('OTHER_HERO'),
                                elements.get('OTHER_POTION_HERO'),
                                elements.get('OTHER_DEAD_HERO'))

    def find_enemy_heroes(self):
        return self._board.find(elements.get('ENEMY_HERO'),
                                elements.get('ENEMY_POTION_HERO'),
                                elements.get('ENEMY_DEAD_HERO'))

    def get_ghosts(self):
        return self._board.find(elements.get('GHOST'))

    def find_barriers(self):
        points = set()
        points.update(self.find_walls())
        points.update(self.find_ghosts())
        points.update(self.find_treasure_boxes())
        points.update(self.find_potions())
        points.update(self.find_other_heroes())
        points.update(self.find_enemy_heroes())
        return sorted(points)

    def find_walls(self):
        return self._board.find(elements.get('WALL'))

    def find_ghosts(self):
        return self._board.find(elements.get('GHOST'))

    def find_treasure_boxes(self):
        return self._board.find(elements.get('TREASURE_BOX'))

    def find_potions(self):
        return self._board.find(elements.get('POTION_TIMER_1'),
                                elements.get('POTION_TIMER_2'),
                                elements.get('POTION_TIMER_3'),
                                elements.get('POTION_TIMER_4'),
                                elements.get('POTION_TIMER_5'),
                                elements.get('POTION_HERO'),
                                elements.get('OTHER_POTION_HERO'),
                                elements.get('ENEMY_POTION_HERO'))

    def find_blasts(self):
        return self._board.find(elements.get('BOOM'))

    def predict_future_blasts(self):
        # TODO: implement
        return []

    def find_perks(self):
        return self._board.find(elements.get('POTION_COUNT_INCREASE'),
                                elements.get('POTION_REMOTE_CONTROL'),
                                elements.get('POTION_IMMUNE'),
                                elements.get('POTION_BLAST_RADIUS_INCREASE'))

    def __str__(self):
        return self._board.__str__() + \
               "\nHero at: " + repr(self.find_hero()) + \
               "\nOther heroes at: " + repr(self.find_other_heroes()) + \
               "\nEnemy heroes at: " + repr(self.find_enemy_heroes()) + \
               "\nGhosts at: " + repr(self.find_ghosts()) + \
               "\nPotions at: " + repr(self.find_potions()) + \
               "\nBlasts at: " + repr(self.find_blasts()) + \
               "\nExpected blasts at: " + repr(self.predict_future_blasts())


if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")