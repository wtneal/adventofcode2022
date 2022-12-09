#!/usr/bin/env python3

import argparse
import sys

_KEY = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}


def _parse_file(in_file: str) -> list[int]:
    """
    Helper function that will parse the file
    """

    rounds: list[tuple(str, str)] = []

    with open(in_file) as f:
        for line in f.readlines():
            opp, me = line.strip().split()
            rounds.append((_KEY[opp], _KEY[me])

    return rounds


def _score_round(shape:str , outcome: str) -> int:
    """ A round score is the sum of the shape selected and the outcome """

    shape_key = {
        'rock': 1,
        'paper': 2,
        'scissors': 3,
    }

    outcome_key = {
        'loss': 0,
        'draw': 3,
        'win': 6,
    }

    return shape_key[shape] + outcome_key[outcome]


def part1(rounds: list[tuple(str, str)]) -> str:
    return ''


def part2(rounds: list[tuple(str, str)]) -> str:
    return ''


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
