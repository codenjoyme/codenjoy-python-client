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

import re
from sys import exc_info
from traceback import print_exception

from lib.websocket import WebSocketApp

URL_REGEX = (
    r"(?P<scheme>http|https)://(?P<host>.+)/codenjoy-contest/board/player/(?P<player>\w+)\?code=(?P<code>\d+)"
)


class WebSocketRunner(WebSocketApp):
    def __init__(self, url, solver, **kwargs):
        self._token = url_to_wstoken(url)
        self._solver = solver
        super().__init__(
            url=self._token,
            header=[],
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
            **kwargs,
        )

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
        print("websocket connection error: " + str(error))

    def _on_close(self, webclient):
        print("websocket connection has been closed")


def url_to_wstoken(url):
    matcher = re.search(URL_REGEX, url)
    if matcher is None:
        raise ValueError("invalid url: " + str(url))
    scheme = "wss" if matcher.group("scheme") == "https" else "ws"
    host = matcher.group("host")
    player = matcher.group("player")
    code = matcher.group("code")
    return f"{scheme}://{host}/codenjoy-contest/ws?user={player}&code={code}"


if __name__ == "__main__":
    raise RuntimeError("This module is not designed to be ran from CLI.")
