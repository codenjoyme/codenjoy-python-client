import unittest

from engine.abstract_board import AbstractBoard, Element
from engine.point import Point


class AbstractBoardTest(unittest.TestCase):
    def test_get_at(self):
        board = AbstractBoard("aaa"
                              "bbb"
                              "ccc")

        self.assertEqual("a", str(board.get_at(0, 2)))
        self.assertEqual("a", str(board.get_at(1, 2)))
        self.assertEqual("a", str(board.get_at(2, 2)))

        self.assertEqual("b", str(board.get_at(0, 1)))
        self.assertEqual("b", str(board.get_at(1, 1)))
        self.assertEqual("b", str(board.get_at(2, 1)))

        self.assertEqual("c", str(board.get_at(0, 0)))
        self.assertEqual("c", str(board.get_at(1, 0)))
        self.assertEqual("c", str(board.get_at(2, 0)))

    def test_get(self):
        board = AbstractBoard(".a."
                              ".aa"
                              "...")

        points = board.get(Element("a"))
        expected = "[1,1][1,2][2,1]"
        actual = ''.join(str(p) for p in points)
        self.assertEqual(expected, actual)

        points = board.get(Element("b"))
        expected = ""
        actual = ''.join(str(p) for p in points)
        self.assertEqual(expected, actual)

    def test_is_at(self):
        board = AbstractBoard("..."
                              ".?."
                              "...")
        self.assertEqual(True, board.is_at(1, 1, '?'))
        self.assertEqual(False, board.is_at(1, 1, '.'))

    def test_get_near(self):
        board = AbstractBoard("abc"
                              "def"
                              "ghi")
        elements_near = board.get_near(1, 1)
        self.assertEqual("fdbh", ''.join(str(e) for e in elements_near))

    def test_is_near(self):
        board = AbstractBoard(".?."
                              "..."
                              "...")
        self.assertEqual(True, board.is_near(1, 1, '?'))

        board = AbstractBoard("..."
                              "..?"
                              "...")
        self.assertEqual(True, board.is_near(1, 1, '?'))

        board = AbstractBoard("..."
                              "..."
                              ".?.")
        self.assertEqual(True, board.is_near(1, 1, '?'))

        board = AbstractBoard("..."
                              "..."
                              "..?")
        self.assertEqual(False, board.is_near(1, 1, '?'))

    def test_count_near(self):
        board = AbstractBoard(".?."
                              "..?"
                              ".?.")
        self.assertEqual(3, board.count_near(1, 1, Element('?')))
        self.assertEqual(0, board.count_near(-1, -1, Element('?')))
        self.assertEqual(0, board.count_near(1, 1, Element('#')))

    def test_strpos2pt(self):
        board = AbstractBoard(".?."
                              "?.."
                              "..?")
        self.assertEqual(Point(1, 2), board._strpos2pt(1))
        self.assertEqual(Point(0, 1), board._strpos2pt(3))
        self.assertEqual(Point(2, 0), board._strpos2pt(8))

    def test_xy2strpos(self):
        board = AbstractBoard(".?."
                              "?.."
                              "..?")
        self.assertEqual(1, board._xy2strpos(1, 2))
        self.assertEqual(3, board._xy2strpos(0, 1))
        self.assertEqual(8, board._xy2strpos(2, 0))


if __name__ == '__main__':
    unittest.main()
