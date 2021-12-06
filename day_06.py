from collections import Counter

import aoc_helper
from aoc_helper import extract_ints, frange, irange, iter, list, range

raw = aoc_helper.fetch(6, 2021)
# raw = "3,4,3,1,2"


def parse_raw():
    return extract_ints(raw)


data = parse_raw()


def part_one():
    fish = data.copy()
    for _ in range(80):
        new_fish = fish.count(0)
        fish.extend(9 for _ in range(new_fish))
        fish = [fish - 1 if fish > 0 else 6 for fish in fish]
    return len(fish)


def create_fish(days_left: int):
    fish = 0
    while days_left > 0:
        fish += 1
        fish += days_left // 7
        days_left -= 8
    return fish


def part_two():
    fish = Counter(data.copy())
    for _ in range(256):
        new_fish = fish[0]
        fish[9] = new_fish
        fish = Counter({k - 1: v for k, v in fish.items()})
        fish[6] += fish[-1]
        fish[-1] = 0
    return sum(fish.values())


aoc_helper.lazy_submit(day=6, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=6, year=2021, solution=part_two)
