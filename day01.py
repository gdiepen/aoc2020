import os
import itertools


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().split("\n")

    lines = [int(x) for x in lines if x != ""]

    total_list = [(x+y, x*y) for x, y in itertools.product(lines, lines) if (x+y) == 2020]

    print(total_list[0])

def part2(input_file):
    with open(input_file) as f:
        lines = f.read().split("\n")

    lines = [int(x) for x in lines if x != ""]

    total_list = [(x+y+z, x*y*z) for x, y, z in itertools.product(lines, lines, lines) if (x+y+z) == 2020]

    print(total_list[0])


if __name__ == "__main__":
    part1("inputs/day_01.txt")
    part2("inputs/day_01.txt")

