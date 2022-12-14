#!/usr/bin/env python3

import argparse
import sys


def part1(in_file: str) -> int:
    overlap_count: int = 0
    with open(in_file) as f:
        for line in f.readlines():
            a, b = line.strip().split(',')
            a1, a2 = [int(i) for i in a.split('-')]
            b1, b2 = [int(i) for i in b.split('-')]

            if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
                overlap_count += 1

    return overlap_count


def part2(in_file: str) -> int:
    overlap_count: int = 0
    with open(in_file) as f:
        for line in f.readlines():
            a, b = line.strip().split(',')
            a1, a2 = [int(i) for i in a.split('-')]
            b1, b2 = [int(i) for i in b.split('-')]

            if b1 <= a1 <= b2 or b1 <= a2 <= b2 or a1 <= b1 <= a2 or a1 <= b2 <= a2:
                overlap_count += 1

    return overlap_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--in_file", help="File used as challenge input")
    parser.add_argument("-o", "--out_file", help="File used for challenge output")
    parser.add_argument("-p", "--print", action=argparse.BooleanOptionalAction, help="Print results to command line")

    args = parser.parse_args()

    with open(args.out_file, "w") as f:
        result1 = part1(args.in_file)
        print(result1, file=f)
        print("", file=f)
        if args.print:
            print(result1)
            print("")


        result2 = part2(args.in_file)
        print(result2, file=f)
        if args.print:
            print(result2)
            print("")
