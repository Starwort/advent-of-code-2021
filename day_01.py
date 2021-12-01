import aoc_helper
from aoc_helper import chunk, chunk_default, extract_ints, iter, range

raw = aoc_helper.fetch(1, 2021)


data = extract_ints(raw)


def part_one():
    first, *rest = data
    increased = 0

    for i in rest:
        if i > first:
            increased += 1
        first = i
    return increased


def part_two():
    first, second, third, *rest = data
    last = first + second + third
    increased = 0

    for i in rest:
        first = second
        second = third
        third = i
        new = first + second + third
        if new > last:
            increased += 1
        last = new

    return increased


aoc_helper.lazy_submit(day=1, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=1, year=2021, solution=part_two)
