import os
import itertools


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().split("\n")
    lines = [x for x in lines if x != ""]


    valid_password = 0
    for x in lines:
        min_max = x.split(" ")[0]
        _min = int(min_max.split("-")[0])
        _max = int(min_max.split("-")[1])

        letter = x.split(" ")[1][0]

        password = list(x.split(" ")[2])


        _count = password.count(letter)

        if _count >= _min  and _count <= _max:
            valid_password += 1

    print(valid_password)


if __name__ == "__main__":
    part1("inputs/day_02.txt")


