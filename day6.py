#!/usr/bin/env python3
import argparse
import collections
import sys


def solve(stream: str, marker_size: int) -> int:
    window = collections.deque()

    for i, char in enumerate(stream, 1):
        # if the char is in the buffer then remove all the items in the
        # buffer before and including the current char
        if char in window:
            tmp = window.popleft()
            while tmp != char:
                tmp = window.popleft()

        window.append(char)

        #print(f'i: {i}; window: {window}, len: {len(window)}')

        if len(window) == marker_size:
            return i
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--in_file", help="File used as challenge input")
    parser.add_argument("-o", "--out_file", help="File used for challenge output")
    parser.add_argument("-p", "--print", action=argparse.BooleanOptionalAction, help="Print results to command line")

    args = parser.parse_args()

    with open(args.out_file, "w") as f_out:
        with open(args.in_file) as f_in:
            stream = f_in.read().rstrip()
            result1 = solve(stream, 4)
            print(result1, file=f_out)
            print("", file=f_out)
            if args.print:
                print(result1)
                print("")

            result2 = solve(stream, 14)
            print(result2, file=f_out)
            if args.print:
                print(result2)
