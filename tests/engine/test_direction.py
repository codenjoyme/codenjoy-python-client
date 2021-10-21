import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from engine import direction
from unittest import TestCase


class TestDirection(TestCase):
    def test_value(self):
        self.assertEqual(0, direction.LEFT.value())
        self.assertEqual(1, direction.RIGHT.value())
        self.assertEqual(2, direction.UP.value())
        self.assertEqual(3, direction.DOWN.value())
        self.assertEqual(4, direction.ACT.value())
        self.assertEqual(5, direction.STOP.value())

    def test_change_x(self):
        self.assertEqual(0, direction.LEFT.change_x(1))
        self.assertEqual(2, direction.RIGHT.change_x(1))
        self.assertEqual(1, direction.UP.change_x(1))
        self.assertEqual(1, direction.DOWN.change_x(1))

    def test_change_y(self):
        self.assertEqual(1, direction.LEFT.change_y(1))
        self.assertEqual(1, direction.RIGHT.change_y(1))
        self.assertEqual(2, direction.UP.change_y(1))
        self.assertEqual(0, direction.DOWN.change_y(1))

    def test_inverted(self):
        self.assertEqual(direction.RIGHT, direction.LEFT.inverted())
        self.assertEqual(direction.LEFT, direction.RIGHT.inverted())
        self.assertEqual(direction.DOWN, direction.UP.inverted())
        self.assertEqual(direction.UP, direction.DOWN.inverted())

    def test_invalid_inverted(self):
        self.assertRaises(ValueError, lambda: direction.ACT.inverted())
        self.assertRaises(ValueError, lambda: direction.STOP.inverted())
