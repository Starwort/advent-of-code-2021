import math
from collections import Counter, defaultdict

import aoc_helper
from aoc_helper import extract_ints, frange, irange, iter, list, map, range, tail_call

raw = aoc_helper.fetch(9, 2021)


def parse_raw():
    points = defaultdict(lambda: -1)
    for y, line in enumerate(raw.splitlines()):
        for x, c in enumerate(line):
            points[x, y] = int(c)
    return points


data = parse_raw()
max_x = max(data.keys(), key=lambda x: x[0])[0]
max_y = max(data.keys(), key=lambda x: x[1])[1]


def part_one():
    total = 0
    for y in irange(0, max_y):
        for x in irange(0, max_x):
            if (
                (data[x, y] < data[x - 1, y] or data[x - 1, y] == -1)
                and (data[x, y] < data[x + 1, y] or data[x + 1, y] == -1)
                and (data[x, y] < data[x, y - 1] or data[x, y - 1] == -1)
                and (data[x, y] < data[x, y + 1] or data[x, y + 1] == -1)
            ):
                total += data[x, y] + 1
    return total


def expand_basin(id, map, x, y):
    if data[x, y] in (9, -1):
        return
    if map[x, y] != -1:
        return
    map[x, y] = id
    expand_basin(id, map, x - 1, y)
    expand_basin(id, map, x + 1, y)
    expand_basin(id, map, x, y - 1)
    expand_basin(id, map, x, y + 1)


def part_two():
    basin_map = defaultdict(lambda: -1)
    current_basin = 0
    for y in irange(0, max_y):
        for x in irange(0, max_x):
            if data[x, y] != 9 and basin_map[x, y] == -1:
                expand_basin(current_basin, basin_map, x, y)
                current_basin += 1

    return math.prod(
        v
        for k, v in Counter(
            list(basin_map.values()).filtered(lambda i: i != -1)
        ).most_common(3)
    )


aoc_helper.lazy_submit(day=9, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=9, year=2021, solution=part_two)
