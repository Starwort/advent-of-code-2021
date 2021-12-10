import aoc_helper
from aoc_helper import extract_ints, frange, irange, iter, list, map, range, tail_call

raw = aoc_helper.fetch(10, 2021)


def parse_raw():
    return list(raw.splitlines())


data = parse_raw()


def parse_corrupt(line):
    stack = []
    for c in line:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack.pop() != "(":
                return c
        elif c == "[":
            stack.append(c)
        elif c == "]":
            if stack.pop() != "[":
                return c
        elif c == "{":
            stack.append(c)
        elif c == "}":
            if stack.pop() != "{":
                return c
        elif c == "<":
            stack.append(c)
        elif c == ">":
            if stack.pop() != "<":
                return c
    return ""


def part_one():
    return (
        data.mapped(parse_corrupt)
        .filtered(None)
        .mapped(lambda i: {")": 3, "]": 57, "}": 1197, ">": 25137}[i])
        .sum()
    )


def autocomplete(line):
    stack = []
    for c in line:
        if c == "(":
            stack.append(c)
        elif c == ")":
            stack.pop()
        elif c == "[":
            stack.append(c)
        elif c == "]":
            stack.pop()
        elif c == "{":
            stack.append(c)
        elif c == "}":
            stack.pop()
        elif c == "<":
            stack.append(c)
        elif c == ">":
            stack.pop()
    stack = stack[::-1]
    score = 0
    for c in stack:
        score *= 5
        score += " ([{<".index(c)
    return score


def part_two():
    new_data = data.filtered(lambda i: parse_corrupt(i) == "")
    return new_data.mapped(autocomplete).median()


aoc_helper.lazy_submit(day=10, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=10, year=2021, solution=part_two)
