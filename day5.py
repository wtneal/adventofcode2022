#!/usr/bin/env python3

import argparse
import collections
import re
import sys


def part1(in_file: str) -> int:
    stacks = []

    with open(in_file) as f:
        # build initial stacks
        # --------------------
        line = next(f).strip()
        raw_stacks = line[1::2][::2]
        stacks = [collections.deque() for _ in range(len(raw_stacks))]

        while not line.replace(' ', '').startswith('12345'):
            # loop over every second item, then remove the spaces between
            # the stacks
            for i, item in enumerate(raw_stacks):
                item = item.strip()
                if item:
                    stacks[i].appendleft(item)

            line = next(f).strip()
            raw_stacks = line[1::2][::2]

        print(f'Stacks: {stacks}')

        # skip blank line after stack definition
        next(f)

        for line in f:
            line = line.strip()
            cnt, src, sink = [int(i) for i in re.search(r'move (\d+) from (\d+) to (\d+)', line).groups()]
            for _ in range(cnt):
                stacks[sink-1].append(stacks[src-1].pop())

            #print(f'Stacks: {stacks}')

        print(f'Stacks: {stacks}')

    return ''.join(s[-1] for s in stacks)


def part2(in_file: str) -> int:
    stacks = []

    with open(in_file) as f:
        # build initial stacks
        # --------------------
        line = next(f).strip()
        raw_stacks = line[1::2][::2]
        stacks = [collections.deque() for _ in range(len(raw_stacks))]

        while not line.replace(' ', '').startswith('12345'):
            # loop over every second item, then remove the spaces between
            # the stacks
            for i, item in enumerate(raw_stacks):
                item = item.strip()
                if item:
                    stacks[i].appendleft(item)

            line = next(f).strip()
            raw_stacks = line[1::2][::2]

        print(f'Stacks: {stacks}')

        # skip blank line after stack definition
        next(f)

        for line in f:
            line = line.strip()
            cnt, src, sink = [int(i) for i in re.search(r'move (\d+) from (\d+) to (\d+)', line).groups()]
            tmp = collections.deque()
            for _ in range(cnt):
                tmp.appendleft(stacks[src-1].pop())
            stacks[sink-1].extend(tmp)

            #print(f'Stacks: {stacks}; move: {cnt} from {src} to {sink}')

        print(f'Stacks: {stacks}')

    return ''.join(s[-1] for s in stacks)


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
