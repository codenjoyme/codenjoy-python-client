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

from engine.direction import *

CRACK_LEFT = Direction("ACT,LEFT", 0, 0)
CRACK_RIGHT = Direction("ACT,RIGHT", 0, 0)
DIE = Direction("ACT(0)", 0, 0)
SHOOT_LEFT = Direction("ACT(1),LEFT", 0, 0)
SHOOT_RIGHT = Direction("ACT(1),RIGHT", 0, 0)
OPEN_DOOR_LEFT = Direction("ACT(2),LEFT", 0, 0)
OPEN_DOOR_RIGHT = Direction("ACT(2),RIGHT", 0, 0)
CLOSE_DOOR_LEFT = Direction("ACT(3),LEFT", 0, 0)
CLOSE_DOOR_RIGHT = Direction("ACT(3),RIGHT", 0, 0)
