#!/usr/bin/env python3

import argparse
import sys


def _parse_file(in_file: str) -> list[int]:
    """
    Helper function that will parse the file by getting the sum of calories for
    each elf. Each elf is defined by a list of numbers separated by a blank line
    """

    elves: list[int] = []
    cal_total: int = 0

    with open(in_file) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                elves.append(cal_total)
                cal_total = 0
            else:
                cal_total += int(line)

    return elves


def part1(elves: list[int]) -> str:
    """Get elf with the most food/cals"""

    return str(max(elves))


def part2(elves: list[int]) -> str:
    """Get the sum of the three elves with the most food"""

    return str(sum(sorted(elves, reverse=True)[:3]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--in_file", help="File used as challenge input")
    parser.add_argument("-o", "--out_file", help="File used for challenge output")

    args = parser.parse_args()

    elves = _parse_file(args.in_file)

    with open(args.out_file, "w") as f:
        result1 = part1(elves)
        print(result1, file=f)
        print("", file=f)

        result2 = part2(elves)
        print(result2, file=f)
