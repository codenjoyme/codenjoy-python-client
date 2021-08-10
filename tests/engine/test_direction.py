import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from engine import direction
from unittest import TestCase


class TestDirection(TestCase):
    def test_value(self):
        self.assertEquals(0, direction.LEFT.value())
        self.assertEquals(1, direction.RIGHT.value())
        self.assertEquals(2, direction.UP.value())
        self.assertEquals(3, direction.DOWN.value())
        self.assertEquals(4, direction.ACT.value())
        self.assertEquals(5, direction.STOP.value())

    def test_change_x(self):
        self.assertEquals(0, direction.LEFT.change_x(1))
        self.assertEquals(2, direction.RIGHT.change_x(1))
        self.assertEquals(1, direction.UP.change_x(1))
        self.assertEquals(1, direction.DOWN.change_x(1))

    def test_change_y(self):
        self.assertEquals(1, direction.LEFT.change_y(1))
        self.assertEquals(1, direction.RIGHT.change_y(1))
        self.assertEquals(2, direction.UP.change_y(1))
        self.assertEquals(0, direction.DOWN.change_y(1))

    def test_inverted(self):
        self.assertEquals(direction.RIGHT, direction.LEFT.inverted())
        self.assertEquals(direction.LEFT, direction.RIGHT.inverted())
        self.assertEquals(direction.DOWN, direction.UP.inverted())
        self.assertEquals(direction.UP, direction.DOWN.inverted())

    def test_invalid_inverted(self):
        self.assertRaises(ValueError, lambda: direction.ACT.inverted())
        self.assertRaises(ValueError, lambda: direction.STOP.inverted())
