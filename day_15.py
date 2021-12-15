from collections import defaultdict
from heapq import heappop, heappush, heappushpop

import aoc_helper
from aoc_helper import (
    decode_text,
    extract_ints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    tail_call,
)

raw = aoc_helper.fetch(15, 2021)


def parse_raw():
    return list(list(map(int, line)) for line in raw.splitlines())


data = parse_raw()


def part_one():
    to_visit = []
    heappush(to_visit, (0, (0, 0)))
    visited = set()
    target = data[0].len() - 1, data.len() - 1
    while True:
        risk, (x, y) = heappop(to_visit)
        if (x, y) in visited:
            continue
        if (x, y) == target:
            return risk
        visited.add((x, y))
        if x > 0:
            heappush(to_visit, (risk + data[y][x - 1], (x - 1, y)))
        if x < target[0]:
            heappush(to_visit, (risk + data[y][x + 1], (x + 1, y)))
        if y > 0:
            heappush(to_visit, (risk + data[y - 1][x], (x, y - 1)))
        if y < target[1]:
            heappush(to_visit, (risk + data[y + 1][x], (x, y + 1)))


def part_two():
    new_data = list(
        row
        + row.mapped(lambda x: x % 9 + 1)
        + row.mapped(lambda x: (x + 1) % 9 + 1)
        + row.mapped(lambda x: (x + 2) % 9 + 1)
        + row.mapped(lambda x: (x + 3) % 9 + 1)
        for row in data
    )
    new_data = list(
        row.mapped(lambda x: (x + increment - 1) % 9 + 1)
        for increment in range(5)
        for row in new_data
    )
    to_visit = []
    heappush(to_visit, (0, (0, 0)))
    visited = set()
    target = new_data[0].len() - 1, new_data.len() - 1
    while True:
        risk, (x, y) = heappop(to_visit)
        if (x, y) in visited:
            continue
        if (x, y) == target:
            return risk
        visited.add((x, y))
        if x > 0:
            heappush(to_visit, (risk + new_data[y][x - 1], (x - 1, y)))
        if x < target[0]:
            heappush(to_visit, (risk + new_data[y][x + 1], (x + 1, y)))
        if y > 0:
            heappush(to_visit, (risk + new_data[y - 1][x], (x, y - 1)))
        if y < target[1]:
            heappush(to_visit, (risk + new_data[y + 1][x], (x, y + 1)))


aoc_helper.lazy_submit(day=15, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=15, year=2021, solution=part_two)
