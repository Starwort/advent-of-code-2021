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

raw = aoc_helper.fetch(13, 2021)
# raw = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5"""


def parse_raw():
    points, instructions = raw.split("\n\n")
    parsed_points = set(extract_ints(points).chunked(2))
    parsed_instructions = list()
    for instruction in instructions.splitlines():
        instruction = instruction.removeprefix("fold along ")
        if instruction[0] == "x":
            parsed_instructions.append((int(instruction[2:]), 0))
        else:
            parsed_instructions.append((0, int(instruction[2:])))
    return parsed_points, parsed_instructions


points, instructions = parse_raw()


def fold(points, instruction):
    x, y = instruction
    new_points = set()
    if x == 0:
        for px, py in points:
            if py > y:
                new_points.add((px, 2 * y - py))
            else:
                new_points.add((px, py))
    else:
        for px, py in points:
            if px > x:
                new_points.add((2 * x - px, py))
            else:
                new_points.add((px, py))
    return new_points


def part_one():
    return len(fold(points, instructions[0]))


def part_two():
    my_points = points
    for instruction in instructions:
        my_points = fold(my_points, instruction)
    max_x = max(point[0] for point in my_points)
    max_y = max(point[1] for point in my_points)
    dots = [[(x, y) in my_points for x in irange(0, max_x)] for y in irange(0, max_y)]
    return decode_text(dots)


aoc_helper.lazy_submit(day=13, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=13, year=2021, solution=part_two)
