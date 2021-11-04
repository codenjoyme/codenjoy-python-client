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

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from unittest import TestCase

from engine.web_socket_runner import url_to_wstoken


class TestWebSocketRunner(TestCase):

    def test_url_to_wstoken_valid_http_url(self):
        self.assertEqual(
            "ws://127.0.0.1:8080/codenjoy-contest/ws?user=793wdxskw521spo4mn1y&code=531459153668826800",
            url_to_wstoken(
                "http://127.0.0.1:8080/codenjoy-contest/board/player/793wdxskw521spo4mn1y?code=531459153668826800"))

    def test_url_to_wstoken_valid_https_url(self):
        self.assertEqual(
            "wss://dojorena.io/codenjoy-contest/ws?user=793wdxskw521spo4mn1y&code=531459153668826800",
            url_to_wstoken(
                "https://dojorena.io/codenjoy-contest/board/player/793wdxskw521spo4mn1y?code=531459153668826800"))

    def test_url_to_wstoken_unsupported_scheme(self):
        self.assertRaises(ValueError, lambda: url_to_wstoken(
            "ftp://dojorena.io/codenjoy-contest/board/player/793wdxskw521spo4mn1y?code=531459153668826800"))

    def test_url_to_wstoken_invalid_host(self):
        self.assertRaises(ValueError, lambda: url_to_wstoken(
            "https://codenjoy-contest/board/player/793wdxskw521spo4mn1y?code=531459153668826800"))

    def test_url_to_wstoken_playedId_contains_non_word_characters(self):
        self.assertRaises(ValueError, lambda: url_to_wstoken(
            "https://dojorena.io/codenjoy-contest/board/player/7**wdxskw521spo4mn1y?code=531459153668826800"))

    def test_url_to_wstoken_code_contains_non_word_characters(self):
        self.assertRaises(ValueError, lambda: url_to_wstoken(
            "https://dojorena.io/codenjoy-contest/board/player/793wdxskw521spo4mn1y?code=AA5459153668826800"))
