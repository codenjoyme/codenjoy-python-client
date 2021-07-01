#!/usr/bin/env python3

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

import re
from sys import exc_info
from traceback import print_exception
from lib.websocket import WebSocketApp

URL_REGEX = '(?P<scheme>http|https)://(?P<host>.*)/codenjoy-contest/board/player/(?P<player>\\w*)\\?code=(?P<code>\\w*)'


class WebSocketRunner(WebSocketApp):
    def __init__(self, url, solver,
                 on_open=None, on_message=None, on_error=None,
                 on_close=None, keep_running=True, get_mask_key=None):
        self._token = self._url_to_wssocket(url)
        self._solver = solver
        super().__init__(self._token, [], _on_open, _on_message, _on_error, _on_close)

    def _url_to_wssocket(self, url):
        matcher = re.search(URL_REGEX, url)
        if matcher is None:
            raise ValueError("invalid url: " + url)
        scheme = 'wss' if matcher.group('scheme') == 'https' else 'ws'
        return "{}://{}/codenjoy-contest/ws?user={}&code={}".format(
            scheme,
            matcher.group('host'),
            matcher.group('player'),
            matcher.group('code'))


def _on_open(webclient):
    print("websocket connection successfully established")


def _on_message(webclient, message):
    try:
        board = message.lstrip("board=")
        webclient.send(webclient._solver.answer(board))
    except Exception as e:
        print("Exception occurred")
        print(e)
        print_exception(*exc_info())


def _on_error(webclient, error):
    print("websocket connection error " + error)


def _on_close(webclient):
    print("websocket connection has been closed")


if __name__ == '__main__':
    raise RuntimeError("This module is not designed to be ran from CLI.")
