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

elements = dict(

        # Empty space (on layer 2) where player can go.

    EMPTY='-',

        # Empty space (on layer 1) where player can go.

    FLOOR='.',

        # Wall (on layer 1).

    ANGLE_IN_LEFT='╔',

        # Wall (on layer 1).

    WALL_FRONT='═',

        # Wall (on layer 1).

    ANGLE_IN_RIGHT='┐',

        # Wall (on layer 1).

    WALL_RIGHT='│',

        # Wall (on layer 1).

    ANGLE_BACK_RIGHT='┘',

        # Wall (on layer 1).

    WALL_BACK='─',

        # Wall (on layer 1).

    ANGLE_BACK_LEFT='└',

        # Wall (on layer 1).

    WALL_LEFT='║',

        # Wall (on layer 1).

    WALL_BACK_ANGLE_LEFT='┌',

        # Wall (on layer 1).

    WALL_BACK_ANGLE_RIGHT='╗',

        # Wall (on layer 1).

    ANGLE_OUT_RIGHT='╝',

        # Wall (on layer 1).

    ANGLE_OUT_LEFT='╚',

        # Wall (on layer 1).

    SPACE=' ',

        # Charging laser machine (on layer 1) pointing left.

    LASER_MACHINE_CHARGING_LEFT='˂',

        # Charging laser machine (on layer 1) pointing right.

    LASER_MACHINE_CHARGING_RIGHT='˃',

        # Charging laser machine (on layer 1) pointing up.

    LASER_MACHINE_CHARGING_UP='˄',

        # Charging laser machine (on layer 1) pointing down.

    LASER_MACHINE_CHARGING_DOWN='˅',

        # Charged laser machine (on layer 1) pointing left.

    LASER_MACHINE_READY_LEFT='◄',

        # Charged laser machine (on layer 1) pointing right.

    LASER_MACHINE_READY_RIGHT='►',

        # Charged laser machine (on layer 1) pointing up.

    LASER_MACHINE_READY_UP='▲',

        # Charged laser machine (on layer 1) pointing down.

    LASER_MACHINE_READY_DOWN='▼',

        # Level start spot (on layer 1).

    START='S',

        # Level exit spot (on layer 1).

    EXIT='E',

        # Hole (on layer 1).

    HOLE='O',

        # Box (on layer 2) that can be moved and jumped over.

    BOX='B',

        # Zombie start spot (on layer 1).

    ZOMBIE_START='Z',

        # Gold (on layer 1).

    GOLD='$',

        # Unstoppable laser perk (on layer 1).

    UNSTOPPABLE_LASER_PERK='l',

        # Death ray perk (on layer 1).

    DEATH_RAY_PERK='r',

        # Unlimited fire perk (on layer 1).

    UNLIMITED_FIRE_PERK='f',

        # Fire perk (on layer 1).

    FIRE_PERK='a',

        # Jump perk (on layer 1).

    JUMP_PERK='j',

        # Move boxes perk (on layer 1).

    MOVE_BOXES_PERK='m',

        # Your hero (on layer 2).

    ROBO='☺',

        # Your hero (on layer 2) falls into a hole.

    ROBO_FALLING='o',

        # Your hero (on layer 3) falling.

    ROBO_FLYING='*',

        # Your hero (on layer 2) died from a laser.

    ROBO_LASER='☻',

        # Other hero (on layer 2).

    ROBO_OTHER='X',

        # Other hero (on layer 2) falls into a hole.

    ROBO_OTHER_FALLING='x',

        # Other hero (on layer 3) falling.

    ROBO_OTHER_FLYING='^',

        # Other hero (on layer 2) died from a laser.

    ROBO_OTHER_LASER='&',

        # Laser (on layer 2) flies to the left.

    LASER_LEFT='←',

        # Laser (on layer 2) flies to the right.

    LASER_RIGHT='→',

        # Laser (on layer 2) flies to the up.

    LASER_UP='↑',

        # Laser (on layer 2) flies to the down.

    LASER_DOWN='↓',

        # Female zombie (on layer 2).

    FEMALE_ZOMBIE='♀',

        # Male zombie (on layer 2).

    MALE_ZOMBIE='♂',

        # Zombie dies (on layer 2).

    ZOMBIE_DIE='✝',

        # Fog of war system layer (on layer 1).

    FOG='F',

        # Background system layer (on layer 2).

    BACKGROUND='G'
)

if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
