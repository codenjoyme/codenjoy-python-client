from unittest import TestCase

from games.mollymage.solver import Solver


class TestSolver(TestCase):

    def test_answer(self):
        message = "board=" \
                  "☼☼☼☼☼" \
                  "☼   ☼" \
                  "☼ ☺ ☼" \
                  "☼   ☼" \
                  "☼☼☼☼☼"
        self.assertEqual("ACT", Solver().answer(message))
