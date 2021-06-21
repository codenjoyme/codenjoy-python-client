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

from engine.abstract_board import AbstractBoard
from engine.point import Point
from games.mollymage.element import Element


class Board(AbstractBoard):
    BLAST_RANGE = 3

    def _line_by_line(self):
        return '\n'.join([self._content[i:i + self._size]
                          for i in range(0, self._len, self._size)])

    def is_my_hero_dead(self):
        return Element('DEAD_HERO').get_char() in self._content

    def get_hero(self):
        points = set()
        points.update(self.get(Element('HERO')))
        points.update(self.get(Element('POTION_HERO')))
        points.update(self.get(Element('DEAD_HERO')))
        return list(points)[0]

    def get_other_heroes(self):
        return self.get(Element('OTHER_HERO'),
                        Element('OTHER_POTION_HERO'),
                        Element('OTHER_DEAD_HERO'))

    def get_ghosts(self):
        return self.get(Element('GHOST'))

    def get_movement_barriers(self):
        points = set()
        points.update(self.get_other_heroes())
        points.update(self.get_walls())
        points.update(self.get_potions())
        points.update(self.get_treasure_box())
        points.update(self.get_ghosts())
        return list(points)

    def get_blast_barriers(self):
        return self.get(Element('WALL'), Element('TREASURE_BOX'))

    def get_walls(self):
        return self.get(Element('WALL'))

    def get_treasure_box(self):
        return self.get(Element('TREASURE_BOX'))

    def get_potions(self):
        return self.get(Element('POTION_TIMER_1'),
                        Element('POTION_TIMER_2'),
                        Element('POTION_TIMER_3'),
                        Element('POTION_TIMER_4'),
                        Element('POTION_TIMER_5'),
                        Element('POTION_HERO'),
                        Element('OTHER_POTION_HERO'))

    def get_blasts(self):
        return self.get(Element('BOOM'))

    def get_future_blasts(self):
        _points = set()
        for _potion in self.get(Element('POTION_TIMER_1')):
            _points.add(Point(_potion.get_x(), _potion.get_y()))
            # right
            for i in range(1, self.BLAST_RANGE + 1):
                _point = Point(_potion.get_x() + i, _potion.get_y())
                if _point.is_bad(self._size) or _point in self.get_blast_barriers():
                    break
                _points.add(_point)
            # left
            for i in range(1, self.BLAST_RANGE + 1):
                _point = Point(_potion.get_x() - i, _potion.get_y())
                if _point.is_bad(self._size) or _point in self.get_blast_barriers():
                    break
                _points.add(_point)
            # up
            for i in range(1, self.BLAST_RANGE + 1):
                _point = Point(_potion.get_x(), _potion.get_y() + i)
                if _point.is_bad(self._size) or _point in self.get_blast_barriers():
                    break
                _points.add(_point)
            # down
            for i in range(1, self.BLAST_RANGE + 1):
                _point = Point(_potion.get_x(), _potion.get_y() - i)
                if _point.is_bad(self._size) or _point in self.get_blast_barriers():
                    break
                _points.add(_point)
        return sorted(_points)

    def get_perks(self):
        points = set()
        points.update(self.get(Element('POTION_BLAST_RADIUS_INCREASE')))
        points.update(self.get(Element('POTION_COUNT_INCREASE')))
        points.update(self.get(Element('POTION_IMMUNE')))
        points.update(self.get(Element('POTION_REMOTE_CONTROL')))
        return list(points)

    def to_string(self):
        return ("{brd}\n"
                "\n"
                "Hero at: {mbm}\n"
                "Other heroes at: {obm}\n"
                "Ghosts at: {mcp}\n"
                "Treasure boxes at: {dwl}\n"
                "Potions at: {bmb}\n"
                "Blasts at: {bls}\n"
                "Expected blasts at: {ebl}".format(brd=self._line_by_line(),
                                                   mbm=self.get_hero(),
                                                   obm=self.get_other_heroes(),
                                                   mcp=self.get_ghosts(),
                                                   dwl=self.get_treasure_box(),
                                                   bmb=self.get_potions(),
                                                   bls=self.get_blasts(),
                                                   ebl=self.get_future_blasts()))
