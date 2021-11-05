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

elements = dict(
    NONE=' ',  # Пустое место – по которому может двигаться детектив

    BRICK='#',  # Cтена в которой можно прострелить дырочку слева или справа от детектива
                # (в зависимости от того, куда он сейчас смотрит)

    PIT_FILL_1='1',  # Стена со временем зарастает. Когда процес начинается - мы видим таймер
    PIT_FILL_2='2',
    PIT_FILL_3='3',
    PIT_FILL_4='4',

    STONE='☼',  # Неразрушаемая стена - в ней ничего прострелить не получится

    CRACK_PIT='*',  # В момент выстрела мы видим процесс так

    CLUE_KNIFE='$',  # Улика нож
    CLUE_GLOVE='&',  # Улика перчатка
    CLUE_RING='@',  # Улика кольцо

    # Твой детектив в зависимости от того, чем он сейчас занят отображается следующими символами
    HERO_DIE='Ѡ',  # Детектив переживает процесс умирания
    HERO_CRACK_LEFT='Я',  # Детектив простреливает слева от себя
    HERO_CRACK_RIGHT='R',  # Детектив простреливает справа от себя
    HERO_LADDER='Y',  # Детектив находится на лестнице
    HERO_LEFT='◄',  # Детектив бежит влево
    HERO_RIGHT='►',  # Детектив бежит вправо
    HERO_FALL=']',  # Детектив падает, смотря влево
    HERO_PIPE_LEFT='{',  # Детектив ползёт по трубе влево
    HERO_PIPE_RIGHT='}',  # Детектив ползёт по трубе вправо
    HERO_PIT='⍃',  # Детектив в яме смотрит влево

    # Тоже твой детектив, но под маскировкой:
    HERO_MASK_DIE='x',  # Детектив-маскировка переживает процесс умирания
    HERO_MASK_CRACK_LEFT='⊰',  # Детектив-маскировка простреливает слева от себя
    HERO_MASK_CRACK_RIGHT='⊱',  # Детектив-маскировка простреливает справа от себя
    HERO_MASK_LADDER='⍬',  # Детектив-маскировка находится на лестнице
    HERO_MASK_LEFT='⊲',  # Детектив-маскировка бежит влево
    HERO_MASK_RIGHT='⊳',  # Детектив-маскировка бежит вправо
    HERO_MASK_FALL='⊅',  # Детектив-маскировка падает, смотря влево
    HERO_MASK_PIPE_LEFT='⋜',  # Детектив-маскировка ползёт по трубе влево
    HERO_MASK_PIPE_RIGHT='⋝',  # Детектив-маскировка ползёт по трубе вправо
    HERO_MASK_PIT='ᐊ',  # Детектив-маскировка в яме смотрит влево

    # Детективы других игроков отображаются так
    OTHER_HERO_DIE='Z',  # Другой детектив переживает процесс умирания
    OTHER_HERO_CRACK_LEFT='⌋',  # Другой детектив простреливает слева от себя       
    OTHER_HERO_CRACK_RIGHT='⌊',  # Другой детектив простреливает справа от себя      
    OTHER_HERO_LADDER='U',  # Другой детектив находится на лестнице
    OTHER_HERO_LEFT=')',  # Другой детектив бежит влево
    OTHER_HERO_RIGHT='(',  # Другой детектив бежит вправо
    OTHER_HERO_FALL='⊐',  # Другой детектив падает, смотря влево        
    OTHER_HERO_PIPE_LEFT='Э',  # Другой детектив ползёт по трубе влево
    OTHER_HERO_PIPE_RIGHT='Є',  # Другой детектив ползёт по трубе вправо
    OTHER_HERO_PIT='ᗉ',  # Другой детектив в яме смотрит влево

    # А если детективы других игроков под маскировкой, то так
    OTHER_HERO_MASK_DIE='⋈',  # Другой детектив-маскировка переживает процесс умирания
    OTHER_HERO_MASK_CRACK_LEFT='⋰',  # Другой детектив-маскировка простреливает слева от себя       
    OTHER_HERO_MASK_CRACK_RIGHT='⋱',  # Другой детектив-маскировка простреливает справа от себя      
    OTHER_HERO_MASK_LEFT='⋊',  # Другой детектив-маскировка находится на лестнице
    OTHER_HERO_MASK_RIGHT='⋉',  # Другой детектив-маскировка бежит влево
    OTHER_HERO_MASK_LADDER='⋕',  # Другой детектив-маскировка бежит вправо
    OTHER_HERO_MASK_FALL='⋣',  # Другой детектив-маскировка падает, смотря влево        
    OTHER_HERO_MASK_PIPE_LEFT='⊣',  # Другой детектив-маскировка ползёт по трубе влево
    OTHER_HERO_MASK_PIPE_RIGHT='⊢',  # Другой детектив-маскировка ползёт по трубе вправо
    OTHER_HERO_MASK_PIT='ᗏ',  # Другой детектив-маскировка в яме смотрит влево

    # Вражеские детективы других игроков отображаются так
    ENEMY_HERO_DIE='Ž',  # Вражеский детектив переживает процесс умирания       
    ENEMY_HERO_CRACK_LEFT='⟧',  # Вражеский детектив простреливает слева от себя       
    ENEMY_HERO_CRACK_RIGHT='⟦',  # Вражеский детектив простреливает справа от себя      
    ENEMY_HERO_LADDER='Ǔ',  # Вражеский детектив находится на лестнице       
    ENEMY_HERO_LEFT='❫',  # Вражеский детектив бежит влево       
    ENEMY_HERO_RIGHT='❪',  # Вражеский детектив бежит вправо       
    ENEMY_HERO_FALL='⋥',  # Вражеский детектив падает, смотря влево        
    ENEMY_HERO_PIPE_LEFT='Ǯ',  # Вражеский детектив ползёт по трубе влево
    ENEMY_HERO_PIPE_RIGHT='Ě',  # Вражеский детектив ползёт по трубе вправо       
    ENEMY_HERO_PIT='⇇',  # Вражеский детектив в яме смотрит влево

    # А если вражеские детективы других игроков под маскировкой, то так
    ENEMY_HERO_MASK_DIE='⧓',  # Вражеский детектив-маскировка переживает процесс умирания       
    ENEMY_HERO_MASK_CRACK_LEFT='⇢',  # Вражеский детектив-маскировка простреливает слева от себя       
    ENEMY_HERO_MASK_CRACK_RIGHT='⇠',  # Вражеский детектив-маскировка простреливает справа от себя      
    ENEMY_HERO_MASK_LEFT='⧒',  # Вражеский детектив-маскировка находится на лестнице       
    ENEMY_HERO_MASK_RIGHT='⧑',  # Вражеский детектив-маскировка бежит влево       
    ENEMY_HERO_MASK_LADDER='≠',  # Вражеский детектив-маскировка бежит вправо       
    ENEMY_HERO_MASK_FALL='⌫',  # Вражеский детектив-маскировка падает, смотря влево        
    ENEMY_HERO_MASK_PIPE_LEFT='❵',  # Вражеский детектив-маскировка ползёт по трубе влево
    ENEMY_HERO_MASK_PIPE_RIGHT='❴',  # Вражеский детектив-маскировка ползёт по трубе вправо       
    ENEMY_HERO_MASK_PIT='⬱',  # Вражеский детектив-маскировка в яме смотрит влево

    # Боты-воры
    ROBBER_LADDER='Q',
    ROBBER_LEFT='«',
    ROBBER_RIGHT='»',
    ROBBER_FALL='‹',
    ROBBER_PIPE_LEFT='<',
    ROBBER_PIPE_RIGHT='>',
    ROBBER_PIT='⍇',

    # Ворота
    OPENED_DOOR_GOLD='⍙',
    OPENED_DOOR_SILVER='⍚',
    OPENED_DOOR_BRONZE='⍜',

    CLOSED_DOOR_GOLD='⍍',
    CLOSED_DOOR_SILVER='⌺',
    CLOSED_DOOR_BRONZE='⌼',

    KEY_GOLD='✦',
    KEY_SILVER='✼',
    KEY_BRONZE='⍟',

    BULLET='•',

    LADDER='H',  # Лестница - по ней можно перемещаться по уровню
    PIPE='~',  # Труба - по ней так же можно перемещаться по уровню, но только горизонтально

    BACKWAY='⊛',  # Черный ход - позволяет скрыто перемещаться в иное место на карте

    MASK_POTION='S'  # Маскировочное зелье - наделяют детектива дополнительными способностями
)

if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
