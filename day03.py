import os
import itertools


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().split("\n")
    lines = [x for x in lines if x != ""]


    
    width = len(lines[0])
    height = len(lines)


    current_x = 0 
    current_y = 0 

    num_trees = 0
    for current_y in range(len(lines)):
        if lines[current_y][current_x] == "#":
            num_trees += 1

        current_x = (current_x + 3) % width

    print(num_trees)


if __name__ == "__main__":
    part1("inputs/day_03.txt")

