#!/usr/bin/env python3

import argparse
import functools
import operator
import sys


def read_grid(in_file: str) -> list[list[int]]:
    grid: list[list[int]] = []
    with open(in_file) as f:
        for line in f.readlines():
            grid.append([int(i) for i in line.strip()])

    return grid


def part1(in_file: str) -> int:
    grid = read_grid(in_file)
    width = len(grid[0])
    height = len(grid)
    #print(grid)

    # Track visibility from all directions
    is_visible = [
        [[True for _ in range(4)] for _ in range(width)] for _ in range(height)
    ]
    N, E, S, W = range(4)

    for row in range(1, height - 1):
        w_max = grid[row][0]
        for col in range(1, width - 1):
            if grid[row][col] > w_max:
                w_max = grid[row][col]
            else:
                is_visible[row][col][W] = False

        e_max = grid[row][-1]
        for col in range(width - 2, 0, -1):
            if grid[row][col] > e_max:
                e_max = grid[row][col]
            else:
                is_visible[row][col][E] = False

    for col in range(1, width - 1):
        n_max = grid[0][col]
        for row in range(1, height - 1):
            if grid[row][col] > n_max:
                n_max = grid[row][col]
            else:
                is_visible[row][col][N] = False

        s_max = grid[-1][col]
        for row in range(height - 2, 0, -1):
            if grid[row][col] > s_max:
                s_max = grid[row][col]
            else:
                is_visible[row][col][S] = False

    """
    import pprint
    pprint.pprint([
        [f"{grid[row][col]} ({'<-' if is_visible[row][col][W] else ''}{'^' if is_visible[row][col][N] else ''}{'->' if is_visible[row][col][E] else ''}{'V' if is_visible[row][col][S] else ''}{'X' if not any(i for i in is_visible[row][col]) else ''})"
        for col in range(width)]
        for row in range(height)
    ])
    """

    return sum(
        any(dir_ for dir_ in is_visible[row][col])
        for row in range(height)
        for col in range(width)
    )


def part2(in_file: str) -> int:
    grid = read_grid(in_file)
    width = len(grid[0])
    height = len(grid)
    #print(grid)

    # Track visibility from all directions
    scenic_view = [[[0 for _ in range(4)] for _ in range(width)] for _ in range(height)]
    N, E, S, W = range(4)

    # for each row/col loop over the elements and track the distance between
    # trees that are the same size or smaller or edge of the boundary
    for row in range(height):
        last_seen = {}
        max_h = 0
        for col in range(width):
            tree = grid[row][col]
            scenic_view[row][col][W] = max(col - last_seen.get(tree, 0), 0)
            for h in range(tree, -1, -1):
                last_seen[h] = col

        last_seen = {}
        for col in range(width - 1, -1, -1):
            loc = width - col - 1
            tree = grid[row][col]
            scenic_view[row][col][E] = max(loc - last_seen.get(grid[row][col], 0), 0)
            for h in range(tree, -1, -1):
                last_seen[h] = loc

    for col in range(width):
        last_seen = {}
        for row in range(height):
            tree = grid[row][col]
            scenic_view[row][col][N] = max(row - last_seen.get(grid[row][col], 0), 0)
            for h in range(tree, -1, -1):
                last_seen[h] = row

        last_seen = {}
        for row in range(height - 1, -1, -1):
            loc = height - row - 1
            tree = grid[row][col]
            scenic_view[row][col][S] = max(loc - last_seen.get(tree, 0), 0)
            for h in range(tree, -1, -1):
                last_seen[h] = loc

    # get the product of all the scenic view distances
    max_view = 0
    for row in range(height):
        for col in range(width):
            sv = functools.reduce(operator.mul, scenic_view[row][col])
            max_view = max(max_view, sv)

    """
    import pprint
    pprint.pprint(scenic_view)
    result = [
        [functools.reduce(operator.mul, scenic_view[row][col]) for col in range(width)]
        for row in range(height)
    ]
    pprint.pprint(result)
    """

    return max_view


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--in_file", help="File used as challenge input")
    parser.add_argument("-o", "--out_file", help="File used for challenge output")
    parser.add_argument(
        "-p",
        "--print",
        action=argparse.BooleanOptionalAction,
        help="Print results to command line",
    )

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
