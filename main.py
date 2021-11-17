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

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from sys import argv

import games.mollymage.solver
import games.clifford.solver
from engine.web_socket_runner import WebSocketRunner


def main():
    game = "mollymage"
    url = "http://127.0.0.1:8080/codenjoy-contest/board/player/0?code=000000000000"

    if len(argv) == 3:
        game = argv[1]
        url = argv[2]

    solver = determine_game_solver(game)
    WebSocketRunner(url, solver).run()


def determine_game_solver(game):
    return {
        "mollymage": games.mollymage.solver.Solver(),
        "clifford": games.clifford.solver.Solver()
    }[game]


if __name__ == '__main__':
    main()
