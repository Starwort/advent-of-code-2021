from collections import defaultdict
from heapq import heappop, heappush, heappushpop

import aoc_helper
from aoc_helper import djikstras, list, map, range

raw = aoc_helper.fetch(15, 2021)


def parse_raw():
    return list(map(int, line).collect() for line in raw.splitlines())


data = parse_raw()


def part_one():
    return djikstras(data)


def part_two():
    new_data = list(
        row
        + row.mapped(lambda x: x % 9 + 1)
        + row.mapped(lambda x: (x + 1) % 9 + 1)
        + row.mapped(lambda x: (x + 2) % 9 + 1)
        + row.mapped(lambda x: (x + 3) % 9 + 1)
        for row in data
    )
    new_data = (
        new_data
        + new_data.mapped(lambda row: row.mapped(lambda x: x % 9 + 1))
        + new_data.mapped(lambda row: row.mapped(lambda x: (x + 1) % 9 + 1))
        + new_data.mapped(lambda row: row.mapped(lambda x: (x + 2) % 9 + 1))
        + new_data.mapped(lambda row: row.mapped(lambda x: (x + 3) % 9 + 1))
    )
    return djikstras(new_data)


aoc_helper.lazy_submit(day=15, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=15, year=2021, solution=part_two)
