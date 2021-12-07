import aoc_helper
from aoc_helper import extract_ints, frange, irange, iter, list, range, tail_call

raw = aoc_helper.fetch(7, 2021)


def parse_raw():
    return extract_ints(raw)


data = parse_raw()


def part_one():
    return min(
        data.mapped(lambda x: abs(x - target)).sum()
        for target in range(data.min(), data.max() + 1)
    )


def tri(x):
    return x * (x + 1) // 2


def part_two():
    return min(
        data.mapped(lambda x: tri(abs(x - target))).sum()
        for target in range(data.min(), data.max() + 1)
    )


aoc_helper.lazy_submit(day=7, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=7, year=2021, solution=part_two)
