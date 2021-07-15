from unittest import TestCase

from engine.point import Point


class TestPoint(TestCase):
    def test_valid_points(self):
        self.assertEquals(True, Point(0, 0).is_valid(10))
        self.assertEquals(True, Point(5, 5).is_valid(10))
        self.assertEquals(True, Point(10, 10).is_valid(10))
        self.assertEquals(True, Point(0, 10).is_valid(10))
        self.assertEquals(True, Point(10, 0).is_valid(10))

    def test_invalid_points(self):
        self.assertEquals(False, Point(-1, 10).is_valid(10))
        self.assertEquals(False, Point(10, -1).is_valid(10))
        self.assertEquals(False, Point(11, 10).is_valid(10))
        self.assertEquals(False, Point(10, 11).is_valid(10))