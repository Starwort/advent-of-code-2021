from copy import deepcopy
from itertools import count

import aoc_helper
from aoc_helper import extract_ints, frange, irange, iter, list, map, range, tail_call

raw = aoc_helper.fetch(11, 2021)


def parse_raw():
    return list(map(lambda line: map(int, line).collect(), raw.splitlines()))


data = parse_raw()


def step(octopodes):
    for row in octopodes:
        for i, octopus in enumerate(row):
            row[i] = octopus + 1

    flashed = set()
    new_flashes = {(1, 1)}
    while new_flashes:
        new_flashes.clear()
        for y, row in enumerate(octopodes):
            for x, octopus in enumerate(row):
                if octopus > 9 and (x, y) not in flashed:
                    flashed.add((x, y))
                    new_flashes.add((x, y))
                    xoff = [x]
                    if x > 0:
                        xoff.append(x - 1)
                    if x < len(row) - 1:
                        xoff.append(x + 1)
                    yoff = [y]
                    if y > 0:
                        yoff.append(y - 1)
                    if y < len(octopodes) - 1:
                        yoff.append(y + 1)
                    for ny in yoff:
                        for nx in xoff:
                            octopodes[ny][nx] += 1
    for x, y in flashed:
        octopodes[y][x] = 0
    return len(flashed)


def part_one():
    levels = deepcopy(data)
    flashes = 0
    for i in range(100):
        flashed = step(levels)
        flashes += flashed
    return flashes


def part_two():
    levels = deepcopy(data)
    for i in count(1):
        if step(levels) == 100:
            return i


aoc_helper.lazy_submit(day=11, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=11, year=2021, solution=part_two)
