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

URL_REGEX = '(?P<scheme>http|https)://(?P<host>.+)/codenjoy-contest/board/player/(?P<player>\\w+)\\?code=(?P<code>\\d+)'


class WebSocketRunner(WebSocketApp):
    def __init__(self, url, solver,
                 on_open=None, on_message=None, on_error=None,
                 on_close=None, keep_running=True, get_mask_key=None):
        self._token = url_to_wstoken(url)
        self._solver = solver
        super().__init__(self._token, [], self._on_open, self._on_message, self._on_error, self._on_close)

    def _on_open(self, webclient):
        print("websocket connection successfully established")

    def _on_message(self, webclient, msg_from_server):
        try:
            solver = webclient._solver
            msg_to_server = solver.answer(msg_from_server)
            webclient.send(msg_to_server)
        except Exception as e:
            print("Exception occurred")
            print(e)
            print_exception(*exc_info())

    def _on_error(self, webclient, error):
        print("websocket connection error " + error)

    def _on_close(self, webclient):
        print("websocket connection has been closed")


def url_to_wstoken(url):
    matcher = re.search(URL_REGEX, url)
    if matcher is None:
        raise ValueError("invalid url: " + str(url))
    scheme = 'wss' if matcher.group('scheme') == 'https' else 'ws'
    return "{}://{}/codenjoy-contest/ws?user={}&code={}".format(
        scheme,
        matcher.group('host'),
        matcher.group('player'),
        matcher.group('code'))


if __name__ == '__main__':
    raise RuntimeError("This module is not designed to be ran from CLI.")
