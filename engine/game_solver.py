#!/usr/bin/env python3

from abc import ABC, abstractmethod


class GameSolver(ABC):
    @abstractmethod
    def answer(self, message):
        ...


if __name__ == '__main__':
    raise RuntimeError("This module is not designed to be ran from CLI")
