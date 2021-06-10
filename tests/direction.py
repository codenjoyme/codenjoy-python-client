import unittest

from engine.direction import Direction


class DirectionTest(unittest.TestCase):
    def test_init(self):
        Direction("LEFT")
        Direction("RIGHT")
        Direction("UP")
        Direction("DOWN")
        Direction("ACT")
        Direction("STOP")
        Direction("NULL")
        with self.assertRaises(ValueError):
            Direction("invalid")

    def test_eq(self):
        self.assertEqual(True, Direction("LEFT").__eq__(Direction("LEFT")))
        self.assertEqual(False, Direction("ACT").__eq__(Direction("LEFT")))

    def test_is_null(self):
        self.assertEqual(True, Direction("NULL").is_null())

    def test_to_string(self):
        self.assertEqual("NULL", Direction("NULL").to_string())

    def test_change_x(self):
        self.assertEqual(0, Direction("DOWN").get_x())
        self.assertEqual(1, Direction("DOWN").change_x(1))

    def test_change_y(self):
        self.assertEqual(1, Direction("DOWN").get_y())
        self.assertEqual(0, Direction("DOWN").change_y(1))

    def test_inverted(self):
        self.assertEqual(Direction("LEFT"), Direction("RIGHT").inverted())
        self.assertEqual(Direction("RIGHT"), Direction("LEFT").inverted())
        self.assertEqual(Direction("UP"), Direction("DOWN").inverted())
        self.assertEqual(Direction("DOWN"), Direction("UP").inverted())
        self.assertEqual(Direction("STOP"), Direction("ACT").inverted())
        self.assertEqual(Direction("STOP"), Direction("STOP").inverted())
        self.assertEqual(Direction("STOP"), Direction("NULL").inverted())


if __name__ == '__main__':
    unittest.main()
