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

raw = aoc_helper.fetch(21, 2021)
# raw = """Player 1 starting position: 4
# Player 2 starting position: 8"""


def parse_raw():
    return extract_ints(raw).chunked(2).mapped(lambda i: i[1])


a, b = parse_raw()


def die_roll(rolls):
    return (rolls % 100) + 1


def part_one(target=1000):
    pos_a = a
    pos_b = b
    score_a = 0
    score_b = 0
    rolls = 0
    turn = 0
    while score_a < target and score_b < target:
        roll = die_roll(rolls) + die_roll(rolls + 1) + die_roll(rolls + 2)
        rolls += 3
        if turn == 0:
            pos_a += roll - 1
            pos_a %= 10
            pos_a += 1
            score_a += pos_a
        else:
            pos_b += roll - 1
            pos_b %= 10
            pos_b += 1
            score_b += pos_b
        turn = 1 - turn
    if turn == 0:
        return score_a * rolls
    else:
        return score_b * rolls


def part_two(target=21):
    states = {}
    states[a, b, 0, 0, 0] = 1
    wins = [0, 0]
    while states:
        old_states = states
        states = defaultdict(int)
        for (pos_a, pos_b, score_a, score_b, turn), count in old_states.items():
            if score_a >= target or score_b >= target:
                wins[score_b >= target] += count
                continue
            for i in irange(1, 3):
                for j in irange(1, 3):
                    for k in irange(1, 3):
                        roll = i + j + k
                        if turn == 0:
                            new_pos_a = (pos_a + roll - 1) % 10 + 1
                            states[
                                new_pos_a, pos_b, score_a + new_pos_a, score_b, 1
                            ] += count
                        else:
                            new_pos_b = (pos_b + roll - 1) % 10 + 1
                            states[
                                pos_a, new_pos_b, score_a, score_b + new_pos_b, 0
                            ] += count
    return max(wins)


aoc_helper.lazy_submit(day=21, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=21, year=2021, solution=part_two)
