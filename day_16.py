from math import prod

import aoc_helper
from aoc_helper import range

raw = aoc_helper.fetch(16, 2021)

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def parse_packet(bits):
    version = int(bits[:3], 2)
    type = int(bits[3:6], 2)
    if type == 4:
        data = []
        idx = 6
        while True:
            segment = bits[idx : idx + 5]
            idx += 5
            data.append(segment[1:])
            if segment[0] == "0":
                break
        data = int("".join(data), 2)
        return idx, (version, type, data)
    else:
        length_id = bits[6]
        if length_id == "0":
            packets_len = int(bits[7:22], 2)
            packets_substr = bits[22 : 22 + packets_len]
            packets = []
            while packets_substr:
                packet_len, packet = parse_packet(packets_substr)
                packets_substr = packets_substr[packet_len:]
                packets.append(packet)
            return 22 + packets_len, (version, type, packets)
        else:
            packets_count = int(bits[7:18], 2)
            packets_substr = bits[18:]
            packets = []
            total_len = 18
            for _ in range(packets_count):
                packet_len, packet = parse_packet(packets_substr)
                packets_substr = packets_substr[packet_len:]
                total_len += packet_len
                packets.append(packet)
            return total_len, (version, type, packets)


def parse_raw():
    bits = "".join(hex_to_bin[ch] for ch in raw)
    return parse_packet(bits)


data = parse_raw()


def part_one():
    total = 0
    to_search = [data]
    while to_search:
        packet = to_search.pop()
        total += packet[0]
        if isinstance(packet[2], list):
            to_search.extend(packet[2])
    return total


def handle_packet(packet):
    version, type, data = packet
    match type:
        case 0:
            return sum(handle_packet(packet) for packet in data)
        case 1:
            return prod(handle_packet(packet) for packet in data)
        case 2:
            return min(handle_packet(packet) for packet in data)
        case 3:
            return max(handle_packet(packet) for packet in data)
        case 4:
            return data
        case 5:
            return handle_packet(data[0]) > handle_packet(data[1])
        case 6:
            return handle_packet(data[0]) < handle_packet(data[1])
        case 7:
            return handle_packet(data[0]) == handle_packet(data[1])


def part_two():
    return handle_packet(data)


aoc_helper.lazy_submit(day=16, year=2021, solution=part_one)
aoc_helper.lazy_submit(day=16, year=2021, solution=part_two)
