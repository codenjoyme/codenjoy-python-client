#!/usr/bin/env python3

from sys import version_info


def main():
    assert version_info[0] == 3, "You should run me with Python 3.x"


if __name__ == '__main__':
    main()
