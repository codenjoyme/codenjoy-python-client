import unittest

from engine.point import Point


class PostTest(unittest.TestCase):
    def test_is_bad(self):
        self.assertEqual(True, Point(-1, 10).is_bad(10))
        self.assertEqual(True, Point(10, -1).is_bad(10))
        self.assertEqual(True, Point(15, 10).is_bad(10))
        self.assertEqual(True, Point(10, 15).is_bad(10))
        self.assertEqual(False, Point(10, 10).is_bad(10))

    def test_eq(self):
        self.assertEqual(True, Point(1, 1).__eq__(Point(1, 1)))
        self.assertEqual(False, Point(1, 0).__eq__(Point(1, 1)))
        self.assertEqual(False, Point(0, 1).__eq__(Point(1, 1)))

    def test_to_string(self):
        self.assertEqual("[1,1]", Point(1, 1).to_string())


if __name__ == '__main__':
    unittest.main()
