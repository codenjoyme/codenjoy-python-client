import unittest

from games.mollymage.mollymage_board import BombermanBoard


class BoardTest(unittest.TestCase):
    def test_get_future_blasts(self):
        board = BombermanBoard(".☼☼.."
                               ".3☼.."
                               ".☼..."
                               "..&2&"
                               "1♥...")
        self.assertEqual("[[0,1], [3,4], [0,3], [3,0], [0,2], [3,3], [3,2]]", ''.join(str(board.get_future_blasts())))


if __name__ == '__main__':
    unittest.main()
