#!/usr/bin/env python

import os
import sys
import math

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_line  # nopep8


def fuel_for_mass(m):
    return math.floor(m / 3) - 2


def fuel_for_module(m):
    mass = m
    total_mass = 0
    while True:
        mass = fuel_for_mass(mass)
        if mass <= 0:
            break
        total_mass += mass
    return total_mass


def p1(lines):
    assert fuel_for_mass(12) == 2
    assert fuel_for_mass(14) == 2
    assert fuel_for_mass(1969) == 654
    assert fuel_for_mass(100756) == 33583
    return sum(fuel_for_mass(m) for m in lines)


def p2(lines):
    assert fuel_for_module(1969) == 966
    assert fuel_for_module(100756) == 50346
    return sum(fuel_for_module(m) for m in lines)


if __name__ == "__main__":
    solve(sys.argv, int_line, p1, p2)
