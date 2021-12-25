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

raw = aoc_helper.fetch(25, 2021)
# raw = """v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>"""


def parse_raw():
    return map(list, raw.splitlines()).collect()


data = parse_raw()


def step(map: list[list[str]]):
    moved = 0
    will_step = []
    for y, row in map.enumerated():
        for x, (from_, to) in enumerate(zip(row[-1:] + row[:-1], row), start=-1):
            if to == "." and from_ == ">":
                will_step.append((x, y))
    for x, y in will_step:
        map[y][x] = "."
        map[y][x + 1] = ">"
    moved += len(will_step)
    will_step.clear()
    for y, (from_, to) in enumerate(zip(map[-1:] + map[:-1], map), start=-1):
        for x, (from_cell, to_cell) in enumerate(zip(from_, to)):
            if to_cell == "." and from_cell == "v":
                will_step.append((x, y))
    for x, y in will_step:
        map[y][x] = "."
        map[y + 1][x] = "v"
    moved += len(will_step)
    return moved


def part_one():
    i = 1
    map = data.deepcopy()
    while step(map):
        i += 1
        # print(i, "\n" + "\n".join("".join(row) for row in map))
    return i


def part_two():
    ...


aoc_helper.lazy_submit(day=25, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=25, year=2021, solution=part_two)
