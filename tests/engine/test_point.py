import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from unittest import TestCase

from engine.point import Point


class TestPoint(TestCase):
    def test_valid_points(self):
        self.assertEqual(True, Point(0, 0).is_valid(10))
        self.assertEqual(True, Point(5, 5).is_valid(10))
        self.assertEqual(True, Point(10, 10).is_valid(10))
        self.assertEqual(True, Point(0, 10).is_valid(10))
        self.assertEqual(True, Point(10, 0).is_valid(10))

    def test_invalid_points(self):
        self.assertEqual(False, Point(-1, 10).is_valid(10))
        self.assertEqual(False, Point(10, -1).is_valid(10))
        self.assertEqual(False, Point(11, 10).is_valid(10))
        self.assertEqual(False, Point(10, 11).is_valid(10))
