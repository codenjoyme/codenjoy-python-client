import unittest

from games.mollymage.solver import Solver


class BoardTest(unittest.TestCase):
    def test_next_step(self):
        board = "☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼" \
                "☼☺        # # ☼" \
                "☼ ☼ ☼ ☼#☼ ☼ ☼ ☼" \
                "☼##           ☼" \
                "☼ ☼ ☼#☼ ☼ ☼ ☼ ☼" \
                "☼   #    # #  ☼" \
                "☼ ☼ ☼ ☼#☼ ☼ ☼ ☼" \
                "☼             ☼" \
                "☼#☼ ☼ ☼#☼ ☼ ☼#☼" \
                "☼  #  #       ☼" \
                "☼ ☼ ☼ ☼ ☼ ☼ ☼#☼" \
                "☼ ##      #   ☼" \
                "☼ ☼ ☼ ☼ ☼ ☼ ☼#☼" \
                "☼ #   #  &    ☼" \
                "☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼"
        self.assertEqual("ACT", Solver().get(board))


if __name__ == '__main__':
    unittest.main()
