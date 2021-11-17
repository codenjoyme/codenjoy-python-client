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

from engine.game_board import GameBoard

from .element import elements


class Board:
    def __init__(self, message):
        self._board = GameBoard(elements.values(), message)

    def is_game_over(self):
        return self._board.find_first(elements.get("HERO_DIE"), elements.get("HERO_MASK_DIE")) is not None

    def find_hero(self):
        points = self._board.find(
            elements.get("HERO_DIE"),
            elements.get("HERO_LADDER"),
            elements.get("HERO_LEFT"),
            elements.get("HERO_RIGHT"),
            elements.get("HERO_FALL"),
            elements.get("HERO_PIPE"),
            elements.get("HERO_PIT"),
            elements.get("HERO_MASK_DIE"),
            elements.get("HERO_MASK_LADDER"),
            elements.get("HERO_MASK_LEFT"),
            elements.get("HERO_MASK_RIGHT"),
            elements.get("HERO_MASK_FALL"),
            elements.get("HERO_MASK_PIPE"),
            elements.get("HERO_MASK_PIT"),
        )

        if not points:
            raise ValueError("Hero element has not been found")
        return points[0]

    def find_other_heroes(self):
        return self._board.find(
            elements.get("OTHER_HERO_DIE"),
            elements.get("OTHER_HERO_LADDER"),
            elements.get("OTHER_HERO_LEFT"),
            elements.get("OTHER_HERO_RIGHT"),
            elements.get("OTHER_HERO_FALL"),
            elements.get("OTHER_HERO_PIPE"),
            elements.get("OTHER_HERO_PIT"),
            elements.get("OTHER_HERO_MASK_DIE"),
            elements.get("OTHER_HERO_MASK_LADDER"),
            elements.get("OTHER_HERO_MASK_LEFT"),
            elements.get("OTHER_HERO_MASK_RIGHT"),
            elements.get("OTHER_HERO_MASK_FALL"),
            elements.get("OTHER_HERO_MASK_PIPE"),
            elements.get("OTHER_HERO_MASK_PIT"),
        )

    def find_enemy_heroes(self):
        return self._board.find(
            elements.get("ENEMY_HERO_DIE"),
            elements.get("ENEMY_HERO_LADDER"),
            elements.get("ENEMY_HERO_LEFT"),
            elements.get("ENEMY_HERO_RIGHT"),
            elements.get("ENEMY_HERO_FALL"),
            elements.get("ENEMY_HERO_PIPE"),
            elements.get("ENEMY_HERO_PIT"),
            elements.get("ENEMY_HERO_MASK_DIE"),
            elements.get("ENEMY_HERO_MASK_LADDER"),
            elements.get("ENEMY_HERO_MASK_LEFT"),
            elements.get("ENEMY_HERO_MASK_RIGHT"),
            elements.get("ENEMY_HERO_MASK_FALL"),
            elements.get("ENEMY_HERO_MASK_PIPE"),
            elements.get("ENEMY_HERO_MASK_PIT"),
        )

    def find_robbers(self):
        return self._board.find(
            elements.get("ROBBER_LADDER"),
            elements.get("ROBBER_LEFT"),
            elements.get("ROBBER_RIGHT"),
            elements.get("ROBBER_FALL"),
            elements.get("ROBBER_PIPE"),
            elements.get("ROBBER_PIT"),
        )

    def find_barriers(self):
        return self._board.find(elements.get("BRICK"), elements.get("STONE"))

    def find_pits(self):
        return self._board.find(
            elements.get("CRACK_PIT"),
            elements.get("PIT_FILL_1"),
            elements.get("PIT_FILL_2"),
            elements.get("PIT_FILL_3"),
            elements.get("PIT_FILL_4"),
        )

    def find_clues(self):
        return self._board.find(elements.get("CLUE_KNIFE"), elements.get("CLUE_GLOVE"), elements.get("CLUE_RING"))

    def find_backways(self):
        return self._board.find(elements.get("BACKWAY"))

    def find_potions(self):
        return self._board.find(elements.get("MASK_POTION"))

    def find_doors(self):
        return self._board.find(
            elements.get("OPENED_DOOR_GOLD"),
            elements.get("OPENED_DOOR_SILVER"),
            elements.get("OPENED_DOOR_BRONZE"),
            elements.get("CLOSED_DOOR_GOLD"),
            elements.get("CLOSED_DOOR_SILVER"),
            elements.get("CLOSED_DOOR_BRONZE"),
        )

    def find_keys(self):
        return self._board.find(elements.get("KEY_GOLD"), elements.get("KEY_SILVER"), elements.get("KEY_BRONZE"))

    def __str__(self):
        return (
            self._board.__str__()
            + "\nHero at: "
            + repr(self.find_hero())
            + "\nOther heroes at: "
            + repr(self.find_other_heroes())
            + "\nEnemy heroes at: "
            + repr(self.find_enemy_heroes())
            + "\nRobbers at: "
            + repr(self.find_robbers())
            + "\nMask potions at: "
            + repr(self.find_potions())
            + "\nKeys at: "
            + repr(self.find_keys())
        )


if __name__ == "__main__":
    raise RuntimeError("This module is not intended to be ran from CLI")
