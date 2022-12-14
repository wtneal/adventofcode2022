#!/usr/bin/env python3

import argparse
import sys

_PLAY_KEY = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}


def _score_round(shape: str, outcome: int) -> int:
    """A round score is the sum of the shape selected and the outcome"""

    shape_key = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    return shape_key[shape] + outcome


def part1(in_file: str) -> int:
    game_total = 0

    game_key = {
        ("rock", "rock"): 3,
        ("rock", "paper"): 6,
        ("rock", "scissors"): 0,
        ("paper", "paper"): 3,
        ("paper", "scissors"): 6,
        ("paper", "rock"): 0,
        ("scissors", "scissors"): 3,
        ("scissors", "rock"): 6,
        ("scissors", "paper"): 0,
    }

    with open(in_file) as f:
        for line in f.readlines():
            opp, me = line.strip().split()
            opp_play = _PLAY_KEY[opp]
            play = _PLAY_KEY[me]

            outcome = game_key[(opp_play, play)]
            score = _score_round(play, outcome)
            # print(f'Opp: {opp_play}; Play: {play} -> {outcome} = {score} [total: {game_total}]')
            game_total += score

    return game_total


def part2(in_file: str) -> int:

    game_total = 0
    outcome_key = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    game_key = {
        ("rock", 3): "rock",
        ("rock", 6): "paper",
        ("rock", 0): "scissors",
        ("paper", 3): "paper",
        ("paper", 6): "scissors",
        ("paper", 0): "rock",
        ("scissors", 3): "scissors",
        ("scissors", 6): "rock",
        ("scissors", 0): "paper",
    }

    with open(in_file) as f:
        for line in f.readlines():
            opp, out = line.strip().split()

            opp_play = _PLAY_KEY[opp]
            outcome = outcome_key[out]

            play = game_key[(opp_play, outcome)]

            game_total += _score_round(play, outcome)

    return game_total


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
