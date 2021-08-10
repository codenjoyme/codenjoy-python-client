#!/usr/bin/env python3

class Direction:
    def __init__(self, name, value, dx, dy):
        self._name = name
        self._value = int(value)
        self._dx = int(dx)
        self._dy = int(dy)

    def value(self):
        return self._value

    def change_x(self, x):
        return x + self._dx

    def change_y(self, y):
        return y + self._dy

    def inverted(self):
        if self == LEFT:
            return RIGHT
        if self == RIGHT:
            return LEFT
        if self == UP:
            return DOWN
        if self == DOWN:
            return UP
        raise ValueError("Cant invert for: " + self.__str__())

    def __str__(self):
        return self._name


LEFT = Direction("LEFT", 0, -1, 0)
RIGHT = Direction("RIGHT", 1, 1, 0)
UP = Direction("UP", 2, 0, 1)
DOWN = Direction("DOWN", 3, 0, -1)
ACT = Direction("ACT", 4, 0, 0)
STOP = Direction("STOP", 5, 0, 0)


if __name__ == '__main__':
    raise RuntimeError("This module is not designed to be ran from CLI")
