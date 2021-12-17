from itertools import count

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

raw = aoc_helper.fetch(17, 2021)

x_min, x_max, y_min, y_max = extract_ints(raw)


def sign(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)


def step(x, y, vx, vy):
    x += vx
    y += vy
    vx -= sign(vx)
    vy -= 1
    return x, y, vx, vy


def tri(x):
    return x * (x + 1) // 2


def part_one():
    min_steps = next(i for i in range(x_min) if (x := tri(i)) >= x_min)
    best_y = 0
    overshot_count = 0
    for vy in count():
        this_vy = vy
        y = 0
        steps = 0
        local_max = 0
        while y > y_min:
            steps += 1
            y += vy
            vy -= 1
            if y > local_max:
                local_max = y
            if y_min <= y <= y_max:
                if steps >= min_steps:
                    print("best:", this_vy, best_y, local_max)
                    best_y = max(best_y, local_max)
                break
        else:
            overshot_count += 1
            if overshot_count > 100:
                break
    return best_y


def part_two():
    count = 0
    for vy in range(y_min, 500):
        ivy = vy
        for vx in range(x_max + 1):
            x = y = 0
            vy = ivy
            while x < x_max and y > y_min:
                x, y, vx, vy = step(x, y, vx, vy)
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    count += 1
                    break
    return count


aoc_helper.lazy_submit(day=17, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=17, year=2021, solution=part_two)
