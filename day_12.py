from collections import defaultdict

import aoc_helper
from aoc_helper import extract_ints, frange, irange, iter, list, map, range, tail_call

raw = aoc_helper.fetch(12, 2021)


def parse_raw():
    links = list(list(line.split("-")) for line in raw.splitlines())
    parsed_links = defaultdict(list)
    for from_, to in links:
        parsed_links[from_].append(to)
        parsed_links[to].append(from_)
    return parsed_links


data = parse_raw()


def gen_paths(visited, current, path):
    if current == "end":
        yield path
        return
    for i in data[current]:
        if i.isupper() or not i in visited:
            yield from gen_paths({*visited, i}, i, [*path, i])


def part_one():
    return len(list(gen_paths({"start"}, "start", ["start"])))


def gen_paths_2(visited, current, path):
    if current == "end":
        yield path
        return
    for i in data[current]:
        if (
            i.isupper()
            or visited.get(i, 0) == 0
            or all(v < 2 for k, v in visited.items() if k.islower() and k != "start")
        ):
            if i == "start":
                continue
            yield from gen_paths_2({**visited, i: visited.get(i, 0) + 1}, i, [*path, i])


def part_two():
    return len(list(gen_paths_2({"start": 2}, "start", ["start"])))


aoc_helper.lazy_submit(day=12, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=12, year=2021, solution=part_two)
