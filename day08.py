import os
import itertools
import re
import collections


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    instructions = [ (x.split(" ")[0], int(x.split(" ")[1])) for x in lines]


    IP = 0
    acc_value = 0 

    IP_executed = {}


    finished = False

    while not finished:
        IP_executed[IP] = True
        op,val = instructions[IP]

        if op == "acc":
            acc_value += val

        if op == "jmp":
            IP += val
        else:
            IP += 1

        if IP_executed.get(IP) is not None:
            print(acc_value)
            finished = True

        if IP > len(instructions):
            finished = True

def run_instructions(instructions):
    IP = 0
    acc_value = 0 

    IP_executed = {}


    finished = False

    while not finished:
        IP_executed[IP] = True
        op,val = instructions[IP]

        if op == "acc":
            acc_value += val

        if op == "jmp":
            IP += val
        else:
            IP += 1

        if IP_executed.get(IP) is not None:
            return None

        if IP >= len(instructions):
            print(acc_value)
            finished = True


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    instructions = [ (x.split(" ")[0], int(x.split(" ")[1])) for x in lines]


    for i in range(len(instructions)):
        _current_instructions = [x for x in instructions]

        if _current_instructions[i][0] == "jmp":
            _current_instructions[i] = ("nop", _current_instructions[i][1])
        elif _current_instructions[i][0] == "nop":
            _current_instructions[i] = ("jmp", _current_instructions[i][1])

        run_instructions(_current_instructions)













    
   
   
if __name__ == "__main__":
    #part1("foo.txt")
    part1("inputs/day_08.txt")
    #part2("foo.txt")
    part2("inputs/day_08.txt")

