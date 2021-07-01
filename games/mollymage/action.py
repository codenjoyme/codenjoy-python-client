#!/usr/bin/env python3

from enum import Enum


class Action(Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    UP = 'UP'
    DOWN = 'DOWN'

    ACT = "ACT"
    STOP = "STOP"

    def __str__(self):
        return self.value


if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
