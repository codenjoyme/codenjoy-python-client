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

elements = dict(

    # your Molly
    HERO = b'\xe2\x98\xba'.decode(),                    # '☺' - This is what she usually looks like
    POTION_HERO = b'\xe2\x98\xbb'.decode(),             # '☻' - This is if she is sitting on own potion
    DEAD_HERO = b'\xd1\xa0'.decode(),                   # 'Ѡ' - Oops, your Molly is dead (don't worry, she will appear somewhere in next move).
                                                        #       You're getting penalty points for each death.

    # other players heroes

    OTHER_HERO = b'\xe2\x99\xa5'.decode(),              # '♥' - This is what other heroes looks like.
    OTHER_POTION_HERO = b'\xe2\x99\xa0'.decode(),       # '♠' - This is if other hero is sitting on own potion.
    OTHER_DEAD_HERO = b'\xe2\x99\xa3'.decode(),         # '♣' - Other hero corpse (it will disappear shortly,
                                                        #       right on the next move).
                                                        #       If you've done it you'll get score points.


    # enemy players heroes
    ENEMY_HERO = b'\xe2\x99\xa1'.decode(),              # '♡' - This is what enemy heroes looks like.
    ENEMY_POTION_HERO = b'\xe2\x99\xa4'.decode(),       # '♤' - This is if enemy hero is sitting on own potion.
    ENEMY_DEAD_HERO = b'\xe2\x99\xa7'.decode(),         # '♧' - Enemy hero corpse (it will disappear shortly,
                                                        #       right on the next move).
                                                        #       If you've done it you'll get score points.

    # the potions
    POTION_TIMER_5 = '5',                               # '5' - After Molly set the potion, the timer starts (5 ticks).
    POTION_TIMER_4 = '4',                               # '4' - This will blow up after 4 ticks.
    POTION_TIMER_3 = '3',                               # '3' - This after 3...
    POTION_TIMER_2 = '2',                               # '2' - Two..
    POTION_TIMER_1 = '1',                               # '1' - One.
    BOOM = b'\xd2\x89'.decode(),                        # '҉' - Boom! this is what is potion does everything that is destroyable got destroyed

    # walls
    WALL = b'\xe2\x98\xbc'.decode(),                    # '☼' - Indestructible wall - it will not fall from potion.
    TREASURE_BOX = '#',                                 # '#' - This is a treasure box, it opens with an explosion.
    OPENING_TREASURE_BOX = 'H',                         # 'H' - this is like a treasure box opens looks like, it will disappear on next move.
                                                        #       if it's you did it - you'll get score points. Perhaps a prize will appear.

    # soulless creatures
    GHOST = '&',                                        # '&' - This guys runs over the board randomly and gets in the way all the time.
                                                        #       If it will touch Molly - she will die. You'd better kill this piece of ... soul,
                                                        #       you'll get score points for it.
    DEAD_GHOST = 'x',                                   # 'x' - this is chopper corpse

    # Perks
    POTION_BLAST_RADIUS_INCREASE = '+',                 # '+' - Potion blast radius increase. Applicable only to new potions. The perk is temporary.
    POTION_COUNT_INCREASE = 'c',                        # 'c' - Increase available potions count. Number of extra potions can be set in settings. Temporary.
    POTION_IMMUNE = 'i',                                # 'i' - Do not die after potion blast (own potion and others as well). Temporary.
    POTION_REMOTE_CONTROL = 'r',                        # 'r' - Potion blast not by timer but by second act.
                                                        #       Number of RC triggers is limited and can be set in settings.
    POISON_THROWER = 'T',                               # 'T' - Hero can shoot by poison cloud                         

    # Space
    NONE = ' '                                          # ' ' - This is the only place where you can move your Molly.
)

if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
