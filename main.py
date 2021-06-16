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


from sys import version_info
from sys import argv
from games.mollymage.mollymage_solver import MollyMageSolver
from engine.webclient import WebClient
from urllib.parse import urlparse, parse_qs


def main():
    assert version_info[0] == 3, "You should run me with Python 3.x"

    game = "bomberman"
    url = "http://localhost:8080/codenjoy-contest/board/player/0?code=000000000000"
    if len(argv) == 3:
        game = argv[1]
        url = argv[2]

    wcl = WebClient(url=get_url_for_ws(url), solver=get_solver_for_ws(game))
    wcl.run_forever()


def get_url_for_ws(url):
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)

    return "{}://{}/codenjoy-contest/ws?user={}&code={}".format('ws' if parsed_url.scheme == 'http' else 'wss',
                                                                parsed_url.netloc,
                                                                parsed_url.path.split('/')[-1],
                                                                query['code'][0])


def get_solver_for_ws(game):
    return {
        "bomberman": MollyMageSolver()
    }[game]


if __name__ == '__main__':
    main()
