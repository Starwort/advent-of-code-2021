import aoc_helper
from aoc_helper import chunk, chunk_default, extract_ints, iter, range

raw = aoc_helper.fetch(2, 2021)


def parse_raw():
    for line in raw.splitlines():
        direction, distance = line.split()
        if direction == "up":
            yield 0, -int(distance)
        elif direction == "down":
            yield 0, int(distance)
        elif direction == "forward":
            yield int(distance), 0


def part_one():
    sum_x, sum_y = 0, 0
    for x, y in parse_raw():
        sum_x += x
        sum_y += y
    return sum_x * sum_y


def part_two():
    sum_x, sum_y, sum_aim = 0, 0, 0
    for x, aim in parse_raw():
        sum_aim += aim
        sum_y += x * sum_aim
        sum_x += x
    return sum_x * sum_y


aoc_helper.lazy_submit(day=2, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=2, year=2021, solution=part_two)
