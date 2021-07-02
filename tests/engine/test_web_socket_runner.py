from unittest import TestCase

from engine.web_socket_runner import url_to_wstoken


class TestWebSocketRunner(TestCase):

    def test_url_to_wstoken_valid_http_url(self):
        self.assertEquals(
            "ws://127.0.0.1:8080/codenjoy-contest/ws?user=793wdxskw521spo4mn1y&code=531459153668826800",
            url_to_wstoken(
                "http://127.0.0.1:8080/codenjoy-contest/board/player/793wdxskw521spo4mn1y?code=531459153668826800"))

    def test_url_to_wstoken_valid_https_url(self):
        self.assertEquals(
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
