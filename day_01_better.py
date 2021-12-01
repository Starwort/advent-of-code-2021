import aoc_helper
from aoc_helper import chunk, chunk_default, extract_ints, iter, range

raw = aoc_helper.fetch(1, 2021)


data = extract_ints(raw)


def part_one():
    return sum(b > a for a, b in iter(data).window(2))


def part_two():
    # b and c are common to both expressions, so can be ignored
    return sum(d > a for a, _, _, d in iter(data).window(4))


aoc_helper.lazy_submit(day=1, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=1, year=2021, solution=part_two)
