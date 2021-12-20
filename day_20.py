from collections import defaultdict

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

raw = aoc_helper.fetch(20, 2021)
# raw = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
# raw = """#.#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#...

# #..#.
# #....
# ##..#
# ..#..
# ..###"""


def parse_raw():
    algorithm, input = raw.split("\n\n")
    input = input.splitlines()
    parsed = defaultdict(bool)
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            parsed[x, y] = char == "#"
    return algorithm, parsed


algorithm, input = parse_raw()


def next_pixel(x, y, input):
    num = (
        input[x + 1, y + 1]
        | (input[x, y + 1] << 1)
        | (input[x - 1, y + 1] << 2)
        | (input[x + 1, y] << 3)
        | (input[x, y] << 4)
        | (input[x - 1, y] << 5)
        | (input[x + 1, y - 1] << 6)
        | (input[x, y - 1] << 7)
        | (input[x - 1, y - 1] << 8)
    )
    return algorithm[num] == "#"


def bounds(image):
    left = min(x - 1 for x, _ in image.keys())
    right = max(x + 1 for x, _ in image.keys())
    top = min(y - 1 for _, y in image.keys())
    bottom = max(y + 1 for _, y in image.keys())
    return left, right, top, bottom


def step_image(image):
    left, right, top, bottom = bounds(image)
    orig_image = image.copy()
    for x in irange(left, right):
        for y in irange(top, bottom):
            image[x, y] = next_pixel(x, y, orig_image)
    if algorithm[0] == "#" and algorithm[-1] == ".":
        curr = image.default_factory()
        image.default_factory = lambda: not curr


def print_image(image):
    left, right, top, bottom = bounds(image)
    for y in irange(top + 1, bottom - 1):
        for x in irange(left + 1, right - 1):
            print("#" if image[(x, y)] else ".", end="")
        print()


def part_one():
    image = input.copy()
    for i in range(2):
        step_image(image)
    return sum(image.values())


def part_two():
    image = input.copy()
    for i in range(50):
        step_image(image)
    return sum(image.values())


aoc_helper.lazy_submit(day=20, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=20, year=2021, solution=part_two)
