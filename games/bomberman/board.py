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
from games.bomberman.element import Element


class Board(AbstractBoard):

    def to_string(self):
        return ("{brd}\n\nBomberman at: {mbm}\nOther Bombermans "
                "at: {obm}\nMeat Choppers at: {mcp}\nDestroy Walls at:"
                " {dwl}\nBombs at: {bmb}\nBlasts at: {bls}\nExpected "
                "Blasts at: {ebl}".format(brd=self._line_by_line(),
                                          mbm=self.get_bomberman(),
                                          obm=self.get_other_bombermans(),
                                          mcp=self.get_meat_choppers(),
                                          dwl=self.get_destroy_walls(),
                                          bmb=self.get_bombs(),
                                          bls=self.get_blasts(),
                                          ebl=self.get_future_blasts())
                )

    def _line_by_line(self):
        return '\n'.join([self._string[i:i + self._size]
                          for i in range(0, self._len, self._size)])

    def is_barrier_at(self, x, y):
        return Point(x, y) in self.get_barriers()

    def is_my_bomberman_dead(self):
        return Element('DEAD_BOMBERMAN').get_char() in self._string

    def get_bomberman(self):
        points = set()
        points.update(self._find_all(Element('BOMBERMAN')))
        points.update(self._find_all(Element('BOMB_BOMBERMAN')))
        points.update(self._find_all(Element('DEAD_BOMBERMAN')))
        assert len(points) <= 1, "There should be only one bomberman"
        return list(points)[0]

    def get_other_bombermans(self):
        points = set()
        points.update(self._find_all(Element('OTHER_BOMBERMAN')))
        points.update(self._find_all(Element('OTHER_BOMB_BOMBERMAN')))
        points.update(self._find_all(Element('OTHER_DEAD_BOMBERMAN')))
        return list(points)

    def get_meat_choppers(self):
        return self._find_all(Element('MEAT_CHOPPER'))

    def get_barriers(self):
        points = set()
        points.update(self.get_walls())
        points.update(self.get_bombs())
        points.update(self.get_destroy_walls())
        points.update(self.get_meat_choppers())
        points.update(self.get_other_bombermans())
        return list(points)

    def get_walls(self):
        return self._find_all(Element('WALL'))

    def get_destroy_walls(self):
        return self._find_all(Element('DESTROY_WALL'))

    def get_bombs(self):
        points = set()
        points.update(self._find_all(Element('BOMB_TIMER_1')))
        points.update(self._find_all(Element('BOMB_TIMER_2')))
        points.update(self._find_all(Element('BOMB_TIMER_3')))
        points.update(self._find_all(Element('BOMB_TIMER_4')))
        points.update(self._find_all(Element('BOMB_TIMER_5')))
        points.update(self._find_all(Element('BOMB_BOMBERMAN')))
        return list(points)

    def get_blasts(self):
        return self._find_all(Element('BOOM'))

    def get_future_blasts(self):
        _bombs = set()
        _bombs.update(self.get_bombs())
        _bombs.update(self._find_all(Element('OTHER_BOMB_BOMBERMAN')))
        _points = set()
        for _bomb in _bombs:
            _bx, _by = _bomb.get_x(), _bomb.get_y()
            _points.add(_bomb)
            _points.update(self._search_blasts(_bomb))
        return [_points]

    def _search_blasts(self, bomb_point):
        points = set()
        walls = self.get_walls()

        for search_range, is_x in ((range(bomb_point.get_x(), bomb_point.get_x() + self.BLAST_RANGE), True),
                                   (range(bomb_point.get_x(), bomb_point.get_x() - self.BLAST_RANGE), True),
                                   (range(bomb_point.get_y(), bomb_point.get_y() + self.BLAST_RANGE), False),
                                   (range(bomb_point.get_y(), bomb_point.get_y() - self.BLAST_RANGE), False)):
            for i in search_range:
                current_point = Point(i, bomb_point.get_y()) if is_x else Point(bomb_point.get_x(), i)
                if (current_point.is_bad(self._size) or
                        current_point in walls):
                    break
                else:
                    points.add(current_point)

        return points

    def get_perks(self):
        points = set()
        points.update(self._find_all(Element('BOMB_BLAST_RADIUS_INCREASE')))
        points.update(self._find_all(Element('BOMB_COUNT_INCREASE')))
        points.update(self._find_all(Element('BOMB_IMMUNE')))
        points.update(self._find_all(Element('BOMB_REMOTE_CONTROL')))
        return list(points)
