




import os
import itertools
import re
import collections


def exists_sum_to(_list, target):
    return len([x+y for x,y in itertools.product(_list, _list) if x+y == target]) > 0


def part1(input_file, preamble_length):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    lines = [int(x) for x in lines]

    i = preamble_length

    for i in range(preamble_length, len(lines)):
        if not exists_sum_to(lines[i-preamble_length:i], lines[i]):
            print(lines[i])



def part2(input_file, preamble_length):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    lines = [int(x) for x in lines]

    i = preamble_length

    TARGET = -1
    for i in range(preamble_length, len(lines)):
        if not exists_sum_to(lines[i-preamble_length:i], lines[i]):
            TARGET = lines[i]


    for i in range(len(lines)):
        acc = lines[i] 
        for j in range(i+1, len(lines)):
            acc += lines[j]

            if acc == TARGET:

                _min = min(lines[i:j+1])
                _max = max(lines[i:j+1])
                print(_min+_max)
                break
            if acc > TARGET:
                break







    
   
   
if __name__ == "__main__":
    part1("inputs/day_09.txt", 25)
    #part2("foo.txt", 5)
    part2("inputs/day_09.txt", 25)


