import os
import itertools
import re


def part1(input_file):
    with open(input_file) as f:

        groups_input = f.read().split("\n\n")
    
    results = []
    for group in groups_input:
        foo = list(group.replace("\n",""))
        foo = set(foo)
        results.append(len(foo))

    print(sum(results))



    




if __name__ == "__main__":
    part1("inputs/day_06.txt")
    #part1("foo.txt")
    #part2("inputs/day_06.txt")

