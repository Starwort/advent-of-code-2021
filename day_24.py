import itertools

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

raw = aoc_helper.fetch(24, 2021)


def decode(reg):
    if i := extract_ints(reg):
        return False, i[0]
    return True, ord(reg) - ord("w")


def parse_raw():
    instructions = list()
    for line in raw.splitlines():
        opcode, *regs = line.split()
        instructions.append((opcode, map(decode, regs).collect()))
    return instructions


data = parse_raw()


def trunc_div(x, y):
    return x // y if x >= 0 else -(-x // y)


def rem(x, y):
    return x % y if x >= 0 else -(-x % y)


def get(vars, arg):
    if arg[0]:
        return vars[arg[1]]
    return arg[1]


def optimised_monad(nums):
    z = nums[0] + 3
    z *= 26
    z += nums[1] + 12
    if True:
        if nums[2] + 3 != nums[3]:
            z *= 26
            z += nums[3] + 12
        if nums[4] - 6 != nums[5]:
            z *= 26
            z += nums[5] + 1
    z, x = divmod(z, 26)
    x -= 4
    if x != nums[6]:
        z *= 26
        z += nums[6] + 1
    z *= 26
    z += nums[7] + 13
    if True:
        z *= 26
        z += nums[8] + 1
        if True:
            if nums[9] - 5 != nums[10]:
                z *= 26
                z += nums[10] + 2
        z, x = divmod(z, 26)
        if x != nums[11]:
            z *= 26
            z += nums[11] + 11
    z, x = divmod(z, 26)
    x -= 8
    if x != nums[12]:
        z *= 26
        z += nums[12] + 10
    z, x = divmod(z, 26)
    x -= 7
    if x != nums[13]:
        z *= 26
        z += nums[13] + 3
    return not z


def run_machine(input_queue):
    vars = [0, 0, 0, 0]
    for opcode, args in data:
        match opcode:
            case "inp":
                vars[args[0][1]] = input_queue.pop(0)
            case "add":
                vars[args[0][1]] += get(vars, args[1])
            case "mul":
                vars[args[0][1]] *= get(vars, args[1])
            case "div":
                vars[args[0][1]] = trunc_div(get(vars, args[0]), get(vars, args[1]))
            case "mod":
                vars[args[0][1]] = rem(get(vars, args[0]), get(vars, args[1]))
            case "eql":
                vars[args[0][1]] = 1 if get(vars, args[0]) == get(vars, args[1]) else 0
    return vars


def part_one():
    best = None
    # for digs in itertools.product(range(1, 10), repeat = 14):
    #     if digs[-5:] == (1,1,1,1,1):
    #         print(digs)
    #     if optimised_monad(digs):
    #         best = digs
    nums = [9] * 14
    nums[2] = 6
    nums[5] = 3
    nums[1] = 1
    nums[10] = 4
    nums[8] = 8
    nums[7] = 4
    nums[13] = 5
    # print(optimised_monad(nums))
    return int("".join(map(str, nums)))


def part_two():
    nums = [1] * 14
    nums[3] = 4
    nums[4] = 7
    nums[6] = 9
    nums[9] = 6
    nums[11] = 2
    nums[12] = 6
    nums[0] = 5
    if optimised_monad(nums):
        return int("".join(map(str, nums)))
    # for digs in itertools.product(range(1, 10), repeat = 14):
    #     if optimised_monad(digs):
    #         return int("".join(map(str, digs)))


aoc_helper.lazy_submit(day=24, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=24, year=2021, solution=part_two)
