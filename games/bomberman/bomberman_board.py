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
from games.bomberman.bomberman_element import BombermanElement


class BombermanBoard(AbstractBoard):
    BLAST_RANGE = 3

    def to_string(self):
        return ("{brd}\n\nHero at: {mbm}\nOther Heroes "
                "at: {obm}\nMeat Choppers at: {mcp}\nDestroy Walls at:"
                " {dwl}\nBombs at: {bmb}\nBlasts at: {bls}\nExpected "
                "Blasts at: {ebl}".format(brd=self._line_by_line(),
                                          mbm=self.get_hero(),
                                          obm=self.get_other_heroes(),
                                          mcp=self.get_meat_choppers(),
                                          dwl=self.get_destroy_walls(),
                                          bmb=self.get_bombs(),
                                          bls=self.get_blasts(),
                                          ebl=self.get_future_blasts())
                )

    def _line_by_line(self):
        return '\n'.join([self._content[i:i + self._size]
                          for i in range(0, self._len, self._size)])

    def is_barrier_at(self, x, y):
        return Point(x, y) in self.get_barriers()

    def is_my_hero_dead(self):
        return BombermanElement('DEAD_HERO').get_char() in self._content

    def get_hero(self):
        points = set()
        points.update(self._find_all(BombermanElement('HERO')))
        points.update(self._find_all(BombermanElement('BOMB_HERO')))
        points.update(self._find_all(BombermanElement('DEAD_HERO')))
        assert len(points) <= 1, "There should be only one hero"
        return list(points)[0]

    def get_other_heroes(self):
        points = set()
        points.update(self._find_all(BombermanElement('OTHER_HERO')))
        points.update(self._find_all(BombermanElement('OTHER_BOMB_HERO')))
        points.update(self._find_all(BombermanElement('OTHER_DEAD_HERO')))
        return list(points)

    def get_meat_choppers(self):
        return self._find_all(BombermanElement('MEAT_CHOPPER'))

    def get_barriers(self):
        points = set()
        points.update(self.get_walls())
        points.update(self.get_bombs())
        points.update(self.get_destroy_walls())
        points.update(self.get_meat_choppers())
        points.update(self.get_other_heroes())
        return list(points)

    def get_walls(self):
        return self._find_all(BombermanElement('WALL'))

    def get_destroy_walls(self):
        return self._find_all(BombermanElement('DESTROY_WALL'))

    def get_bombs(self):
        points = set()
        points.update(self._find_all(BombermanElement('BOMB_TIMER_1')))
        points.update(self._find_all(BombermanElement('BOMB_TIMER_2')))
        points.update(self._find_all(BombermanElement('BOMB_TIMER_3')))
        points.update(self._find_all(BombermanElement('BOMB_TIMER_4')))
        points.update(self._find_all(BombermanElement('BOMB_TIMER_5')))
        points.update(self._find_all(BombermanElement('BOMB_HERO')))
        points.update(self._find_all(BombermanElement('OTHER_BOMB_HERO')))
        return list(points)

    def get_blasts(self):
        return self._find_all(BombermanElement('BOOM'))

    def get_future_blasts(self):
        _points = set()
        for _bomb in self.get_bombs():
            # right
            for i in range(1, self.BLAST_RANGE + 1):
                _point = Point(_bomb.get_x() + i, _bomb.get_y())
                if _point.is_bad(self._size) or _point in self.get_barriers():
                    break
                _points.add(_point)
            # left
            for i in range(1, self.BLAST_RANGE + 1):
                _point = Point(_bomb.get_x() - i, _bomb.get_y())
                if _point.is_bad(self._size) or _point in self.get_barriers():
                    break
                _points.add(_point)
            # up
            for i in range(1, self.BLAST_RANGE + 1):
                _point = Point(_bomb.get_x(), _bomb.get_y() + i)
                if _point.is_bad(self._size) or _point in self.get_barriers():
                    break
                _points.add(_point)
            # down
            for i in range(1, self.BLAST_RANGE + 1):
                _point = Point(_bomb.get_x(), _bomb.get_y() - i)
                if _point.is_bad(self._size) or _point in self.get_barriers():
                    break
                _points.add(_point)
        return list(_points)

    def get_perks(self):
        points = set()
        points.update(self._find_all(BombermanElement('BOMB_BLAST_RADIUS_INCREASE')))
        points.update(self._find_all(BombermanElement('BOMB_COUNT_INCREASE')))
        points.update(self._find_all(BombermanElement('BOMB_IMMUNE')))
        points.update(self._find_all(BombermanElement('BOMB_REMOTE_CONTROL')))
        return list(points)
