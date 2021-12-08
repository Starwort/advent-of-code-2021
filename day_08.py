import itertools

import aoc_helper
from aoc_helper import extract_ints, frange, irange, iter, list, range, tail_call

raw = aoc_helper.fetch(8, 2021)


def convert(segments):
    return list(map(lambda d: ord(d) - ord("a"), segments))


def parse_raw():
    for line in raw.splitlines():
        signals, output = line.split(" | ")
        yield list(map(convert, signals.split())), list(map(convert, output.split()))


data = list(parse_raw())


def part_one():
    return (
        data.mapped(lambda x: x[1])
        .mapped(lambda x: sum(len(d) in {2, 3, 4, 7} for d in x))
        .sum()
    )


def part_two():
    total = 0
    for signals, outputs in data:
        for a, b, c, d, e, f, g in itertools.permutations(range(7)):
            digits = {
                frozenset((a, b, c, e, f, g)): 0,
                frozenset((c, f)): 1,
                frozenset((a, c, d, e, g)): 2,
                frozenset((a, c, d, f, g)): 3,
                frozenset((b, c, d, f)): 4,
                frozenset((a, b, d, f, g)): 5,
                frozenset((a, b, d, e, f, g)): 6,
                frozenset((a, c, f)): 7,
                frozenset((a, b, c, d, e, f, g)): 8,
                frozenset((a, b, c, d, f, g)): 9,
            }
            bad = False
            for signal in signals:
                key = frozenset(segment for segment in signal)
                if key not in digits:
                    bad = True
            for output in outputs:
                key = frozenset(segment for segment in output)
                if key not in digits:
                    bad = True
            if not bad:
                value = 0
                for output in outputs:
                    key = frozenset(segment for segment in output)
                    value *= 10
                    value += digits[key]
                total += value
                break
    return total


aoc_helper.lazy_submit(day=8, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=8, year=2021, solution=part_two)
