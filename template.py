#!/usr/bin/env python3

import argparse
import sys


def part1(in_file: str) -> int:
    with open(in_file) as f:
        for line in f.readlines():
            pass

    return 0


def part2(in_file: str) -> int:
    with open(in_file) as f:
        for line in f.readlines():
            pass

    return 0


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
