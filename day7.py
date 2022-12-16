#!/usr/bin/env python3

import argparse
import re
import sys

class Node:
    def __init__(self, name:str, parent, size:int=0):
        self.name = name
        self.size:int = size
        self.parent:Node = parent
        self.children: list[Node] =[]

    def __str__(self):
        return f'{"D " if self.children else ""}{self.name}({self.size}){" -> " if self.children else ""}{list(str(c) for c in self.children) if self.children else ""}'


def calc_size(n: Node):
    for c in n.children:
        calc_size(c)
        n.size += c.size
    return n.size



def part1(in_file: str) -> int:
    root = Node('/', None)
    curr = root

    with open(in_file) as f:
        for line in f.readlines():
            line = line.strip()
            #print(line)

            if line.startswith('$ ls'):
                pass
            elif line.startswith('$ cd'):
                dir_name = re.search(r'\$ cd (.*)$', line).group(1)
                if dir_name == '/':
                    curr = root
                elif dir_name == '..':
                    #print(f'changing from {curr.name} to {curr.parent.name}')
                    curr = curr.parent
                else:
                    # find the directory to change to
                    for child in curr.children:
                        if child.name == dir_name:
                            #print(f'changing from {curr.name} to {child.name}')
                            curr = child
                            break

            elif line.startswith('dir '):
                dir_name = re.search(r'dir (.*)$', line).group(1)
                curr.children.append(Node(dir_name, curr))
            else:
                size, file_name = re.search(r'(\d+) (.*)$', line).groups()
                curr.children.append(Node(file_name, curr, int(size)))


    calc_size(root)
    print(root)

    def traverse(n: Node, max_size:int=0):
        dirs = []
        if n.size <= max_size and n.children:
            print(n.name, n.size)
            dirs.append(n)

        for c in n.children:
            dirs.extend(traverse(c, max_size))

        return dirs

    dirs = traverse(root, 100000)
    #print(list(d.size for d in dirs))

    return sum(d.size for d in dirs)


def part2(in_file: str) -> int:
    root = Node('/', None)
    curr = root

    with open(in_file) as f:
        for line in f.readlines():
            line = line.strip()
            #print(line)

            if line.startswith('$ ls'):
                pass
            elif line.startswith('$ cd'):
                dir_name = re.search(r'\$ cd (.*)$', line).group(1)
                if dir_name == '/':
                    curr = root
                elif dir_name == '..':
                    #print(f'changing from {curr.name} to {curr.parent.name}')
                    curr = curr.parent
                else:
                    # find the directory to change to
                    for child in curr.children:
                        if child.name == dir_name:
                            #print(f'changing from {curr.name} to {child.name}')
                            curr = child
                            break

            elif line.startswith('dir '):
                dir_name = re.search(r'dir (.*)$', line).group(1)
                curr.children.append(Node(dir_name, curr))
            else:
                size, file_name = re.search(r'(\d+) (.*)$', line).groups()
                curr.children.append(Node(file_name, curr, int(size)))


    calc_size(root)

    free_space = 70_000_000 - root.size

    def traverse(n: Node, needed_space:int=0,free_space:int=0):
        dirs = []
        if n.size + free_space >= needed_space and n.children:
            print(n.name, n.size)
            dirs.append(n)

        for c in n.children:
            dirs.extend(traverse(c, needed_space, free_space))

        return dirs

    dirs = traverse(root, 30_000_000, free_space)

    return min(d.size for d in dirs)


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
