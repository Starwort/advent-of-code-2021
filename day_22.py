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

raw = aoc_helper.fetch(22, 2021)


def parse_raw():
    return list(
        (
            line.split()[0] == "on",
            extract_ints(line).chunked(2).mapped(lambda i: (i[0], i[1] + 1)),
        )
        for line in raw.splitlines()
    )


data = parse_raw()


def part_one():
    core = defaultdict(bool)
    for value, (xr, yr, zr) in data:
        for x in range(*xr):
            if -50 > x or 50 < x:
                continue
            for y in range(*yr):
                if -50 > y or 50 < y:
                    continue
                for z in range(*zr):
                    if -50 > z or 50 < z:
                        continue
                    core[x, y, z] = value
    return sum(core.values())


def minmax(l):
    return (min(l), max(l))


def sum_region(region):
    xr, yr, zr = region
    return (xr[1] - xr[0]) * (yr[1] - yr[0]) * (zr[1] - zr[0])


def part_two():
    regions = list()
    for value, (xr, yr, zr) in data:
        for i, (rx, ry, rz) in regions.enumerated().reversed():
            overlap_x = xr[1] > rx[0] and xr[0] < rx[1]
            overlap_y = yr[1] > ry[0] and yr[0] < ry[1]
            overlap_z = zr[1] > rz[0] and zr[0] < rz[1]
            if overlap_x and overlap_y and overlap_z:
                regions.pop(i)
                if rx[0] < xr[0]:
                    # left
                    regions.append(((rx[0], xr[0]), ry, rz))
                    rx = (xr[0], rx[1])
                if rx[1] > xr[1]:
                    # right
                    regions.append(((xr[1], rx[1]), ry, rz))
                    rx = (rx[0], xr[1])
                if ry[0] < yr[0]:
                    # top
                    regions.append((rx, (ry[0], yr[0]), rz))
                    ry = (yr[0], ry[1])
                if ry[1] > yr[1]:
                    # bottom
                    regions.append((rx, (yr[1], ry[1]), rz))
                    ry = (ry[0], yr[1])
                if rz[0] < zr[0]:
                    # front
                    regions.append((rx, ry, (rz[0], zr[0])))
                    rz = (zr[0], rz[1])
                if rz[1] > zr[1]:
                    # back
                    regions.append((rx, ry, (zr[1], rz[1])))
                    rz = (rz[0], zr[1])
        if value:
            regions.append((minmax(xr), minmax(yr), minmax(zr)))
    return sum(map(sum_region, regions))


aoc_helper.lazy_submit(day=22, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=22, year=2021, solution=part_two)
