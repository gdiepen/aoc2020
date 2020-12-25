import os
import copy
import itertools
import re
import collections
import math


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    earliest_time = int(lines[0])

    bus_ids = [int(x) for x in lines[1].split(",") if x!="x"]



    
    busses = [ (x, x * math.ceil(earliest_time /x )) for x in bus_ids]


    busses = sorted(busses, key=lambda x: x[1])

    print(busses[0][0] * (busses[0][1] - earliest_time))

def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    bus_ids = [(i,int(x)) for i,x in enumerate(lines[1].split(",")) if x != "x"]

    print(bus_ids)


    current_increasor = 1
    current_timestamp = 0


    for i,bus_id in bus_ids:

        print(f"Adding bus {bus_id} with offset {i}")

        while (current_timestamp + i) % bus_id != 0:
            current_timestamp += current_increasor

        current_increasor *= bus_id

        print(f"Current timestamp = {current_timestamp}")


if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_13.txt")
    part2("foo.txt")
    part2("inputs/day_13.txt")
