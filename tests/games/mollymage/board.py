import unittest

from games.mollymage.board import Board

board = Board(
    "☼☼☼☼☼☼☼☼☼"
    "☼1 ♣   ♠☼"
    "☼#2  &  ☼"
    "☼# 3 ♣ ♠☼"
    "☼☺  4   ☼"
    "☼   ♥ H☻☼"
    "☼x H ҉҉҉☼"
    "☼& &    ☼"
    "☼☼☼☼☼☼☼☼☼")


class BoardTest(unittest.TestCase):
    def test_to_string(self):
        expected = "☼☼☼☼☼☼☼☼☼\n"\
                   "☼1 ♣   ♠☼\n"\
                   "☼#2  &  ☼\n"\
                   "☼# 3 ♣ ♠☼\n"\
                   "☼☺  4   ☼\n"\
                   "☼   ♥ H☻☼\n"\
                   "☼x H ҉҉҉☼\n"\
                   "☼& &    ☼\n"\
                   "☼☼☼☼☼☼☼☼☼\n"\
                   "\n"\
                   "Hero at: [1,4]\n" \
                   "Other heroes at: [[3,7], [4,3], [5,5], [7,5], [7,7]]\n"\
                   "Ghosts at: [[1,1], [3,1], [5,6]]\n"\
                   "Treasure boxes at: [[1,5], [1,6]]\n"\
                   "Potions at: [[1,7], [2,6], [3,5], [4,4], [7,3], [7,5], [7,7]]\n"\
                   "Blasts at: [[5,2], [6,2], [7,2]]\n"\
                   "Expected blasts at: [[1,7], [2,7], [3,7], [4,7]]"
        self.assertEqual(expected, board.to_string())


if __name__ == '__main__':
    unittest.main()
