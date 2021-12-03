from functools import partial

import aoc_helper
from aoc_helper import chunk, chunk_default, extract_ints, iter, list, range

raw = list(aoc_helper.fetch(3, 2021).splitlines())


def parse_raw():
    return list(raw).mapped(partial(int, base=2))


data = parse_raw()


def part_one():
    bits = list([0, 0] for bit in raw[0])
    for number in raw:
        for i, bit in enumerate(number):
            bits[i][int(bit)] += 1
    gamma = bits.mapped(lambda x: 0 if x[0] > x[1] else 1).reduce(
        lambda a, b: (a << 1) + b, 0
    )
    epsilon = bits.mapped(lambda x: 1 if x[0] > x[1] else 0).reduce(
        lambda a, b: (a << 1) + b, 0
    )
    return gamma * epsilon


def filter(numbers, position, most=True):
    if len(numbers) == 1:
        return numbers[0]
    bits = [0, 0]
    for number in numbers:
        bits[int(number[position])] += 1
    if most:
        bit = "0" if bits[0] > bits[1] else "1"
    else:
        bit = "1" if bits[0] > bits[1] else "0"
    return filter(numbers.filtered(lambda x: x[position] == bit), position + 1, most)


def part_two():
    return int(filter(raw, 0, False), base=2) * int(filter(raw, 0, True), base=2)


aoc_helper.lazy_submit(day=3, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=3, year=2021, solution=part_two)
