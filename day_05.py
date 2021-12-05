import aoc_helper
from aoc_helper import chunk, chunk_default, extract_ints, iter, list, range

raw = aoc_helper.fetch(5, 2021)


def parse_raw():
    for line in raw.splitlines():
        a, b = line.split(" -> ")
        x1, y1 = a.split(",")
        x2, y2 = b.split(",")
        yield int(x1), int(y1), int(x2), int(y2)


data = list(parse_raw())

max_x = max(max(x1, x2) for x1, _, x2, _ in data)
max_y = max(max(y1, y2) for _, y1, _, y2 in data)


def part_one():
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x1, y1, x2, y2 in data:
        if x1 == x2:
            if y2 < y1:
                y2, y1 = y1, y2
            for y in range(y1, y2 + 1):
                grid[y][x1] += 1
        elif y1 == y2:
            if x2 < x1:
                x2, x1 = x1, x2
            for x in range(x1, x2 + 1):
                grid[y1][x] += 1
    return sum(sum(map(lambda i: i > 1, row)) for row in grid)


def part_two():
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x1, y1, x2, y2 in data:
        if x1 == x2:
            if y2 < y1:
                y2, y1 = y1, y2
            for y in range(y1, y2 + 1):
                grid[y][x1] += 1
        elif y1 == y2:
            if x2 < x1:
                x2, x1 = x1, x2
            for x in range(x1, x2 + 1):
                grid[y1][x] += 1
        else:
            if y1 < y2:
                y_range = range(y1, y2 + 1)
            else:
                y_range = range(y1, y2 - 1, -1)
            if x1 < x2:
                x_range = range(x1, x2 + 1)
            else:
                x_range = range(x1, x2 - 1, -1)
            for y, x in zip(y_range, x_range):
                grid[y][x] += 1
    return sum(sum(map(lambda i: i > 1, row)) for row in grid)


aoc_helper.lazy_submit(day=5, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=5, year=2021, solution=part_two)
