from collections import Counter, defaultdict

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

raw = aoc_helper.fetch(14, 2021)


def parse_raw():
    chain, rules = raw.split("\n\n")
    rules = dict(line.split(" -> ") for line in rules.splitlines())
    return chain, rules


chain, rules = parse_raw()


def step(chain):
    new_chain = []
    for a, b in zip(chain, chain[1:]):
        new_chain.append(a)
        if a + b in rules:
            new_chain.append(rules[a + b])
    new_chain.append(b)
    return "".join(new_chain)


def part_one():
    my_chain = chain
    for i in range(10):
        my_chain = step(my_chain)
    counted = Counter(my_chain)
    return max(counted.values()) - min(counted.values())


def step_pairs(pairs):
    new_out = defaultdict(int)
    for pair, count in pairs.items():
        if pair in rules:
            left_pair = pair[0] + rules[pair]
            right_pair = rules[pair] + pair[1]
            new_out[left_pair] += count
            new_out[right_pair] += count
        else:
            new_out[pair] += count
    return new_out


def part_two():
    pairs = Counter(a + b for a, b in zip(chain, chain[1:]))
    extras = chain[0], chain[-1]
    for i in range(40):
        pairs = step_pairs(pairs)
    final = defaultdict(int)
    for pair, count in pairs.items():
        final[pair[0]] += count
        final[pair[1]] += count
    final[extras[0]] += 1
    final[extras[1]] += 1
    counted = {k: v // 2 for k, v in final.items()}
    return max(counted.values()) - min(counted.values())


aoc_helper.lazy_submit(day=14, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=14, year=2021, solution=part_two)
