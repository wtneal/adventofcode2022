#!/usr/bin/env python3

import argparse
import functools
import sys


def _calc_priority(item: str) -> int:
    offset = 96 if item.islower() else 38
    return ord(item) - offset


def part1(in_file: str) -> int:

    priority_sum = 0

    with open(in_file) as f:
        for line in f.readlines():
            line = line.strip()
            mid = len(line) // 2
            left_items = set(line[:mid])
            right_items = set(line[mid:])

            intersect = left_items.intersection(right_items)
            item = left_items.intersection(right_items).pop()

            priority_sum += _calc_priority(item)
            #print(f'Intersect: {intersect}; Item: {item}; Offset: {offset}; Priority Sum: {priority_sum}')

    return priority_sum


def part2(in_file: str) -> int:
    priority_sum = 0

    with open(in_file) as f:
        lines = list(l.strip() for l in f.readlines())
        for i in range(0, len(lines), 3):
            a, *rest = lines[i:i+3]
            badge = functools.reduce(set(a).intersection, rest).pop()

            priority_sum += _calc_priority(badge)

    return priority_sum


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--in_file", help="File used as challenge input")
    parser.add_argument("-o", "--out_file", help="File used for challenge output")

    args = parser.parse_args()

    with open(args.out_file, "w") as f:
        result1 = part1(args.in_file)
        print(result1, file=f)
        print("", file=f)

        result2 = part2(args.in_file)
        print(result2, file=f)
