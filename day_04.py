import aoc_helper
from aoc_helper import chunk, chunk_default, extract_ints, iter, list, range

raw = aoc_helper.fetch(4, 2021)


def parse_raw():
    nums, *boards = raw.split("\n\n")
    nums = extract_ints(nums)
    boards = list(
        list(extract_ints(line) for line in board.splitlines()) for board in boards
    )
    return nums, boards


nums, boards = parse_raw()


def part_one():
    board_completion = [
        [[False for i in range(5)] for i in range(5)] for board in boards
    ]
    for num in nums:
        for board, completion in zip(boards, board_completion):
            for row in range(5):
                for col in range(5):
                    if board[row][col] == num:
                        completion[row][col] = True
                        break
                else:
                    continue
                break
        for board, numbers in zip(board_completion, boards):
            if any(all(row) for row in board) or any(all(col) for col in zip(*board)):
                return (
                    sum(
                        i
                        for row, crow in zip(numbers, board)
                        for i, c in zip(row, crow)
                        if not c
                    )
                    * num
                )


def part_two():
    board_completion = [
        [[False for i in range(5)] for i in range(5)] for board in boards
    ]
    finished_order = []
    finished = set()
    for num in nums:
        for board, completion in zip(boards, board_completion):
            for row in range(5):
                for col in range(5):
                    if board[row][col] == num:
                        completion[row][col] = True
                        break
                else:
                    continue
                break
        stop = True
        for i, board in enumerate(board_completion):
            if any(all(row) for row in board) or any(all(col) for col in zip(*board)):
                if i not in finished:
                    finished_order.append((i, num))
                    finished.add(i)
                continue
            stop = False
        if stop:
            break
    i, num = finished_order[-1]

    numbers = boards[i]
    board = board_completion[i]
    return (
        sum(i for row, crow in zip(numbers, board) for i, c in zip(row, crow) if not c)
        * num
    )


aoc_helper.lazy_submit(day=4, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=4, year=2021, solution=part_two)
