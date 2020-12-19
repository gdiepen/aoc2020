import os
import itertools
import re
import collections


def part1(input_file):
    with open(input_file) as f:

        groups_input = f.read().split("\n\n")
    
    results = []
    for group in groups_input:
        foo = list(group.replace("\n",""))
        foo = set(foo)
        results.append(len(foo))

    print(sum(results))



def part2(input_file):
    with open(input_file) as f:

        groups_input = f.read().split("\n\n")
    
    results = []
    for group in groups_input:


        c = collections.Counter(list(group.strip().replace("\n","")))
        num_people = len(group.strip().split("\n"))

        all_yes = [letter for letter,count in c.most_common() if count == num_people]


        results.append(len(all_yes))

    print(sum(results))




    




if __name__ == "__main__":
    part1("inputs/day_06.txt")
    #part2("foo.txt")
    #part1("foo.txt")
    part2("inputs/day_06.txt")

