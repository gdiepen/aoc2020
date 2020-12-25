import os
import copy
import itertools
import re
import collections
import math

def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")


    CURRENT_MASK = ""
    fix_0 = 0
    fix_1 = 0

    mem = {}
    for i in lines:
        if i.startswith("mask"):
            CURRENT_MASK = i.split(" = ")[1]

            fix_0 = int(CURRENT_MASK.replace("X", "1"), 2)
            fix_1 = int(CURRENT_MASK.replace("X", "0"), 2)

        if i.startswith("mem"):
            mem_address = i.split("] =")[0].replace("mem[", "")
            value = int(i.split(" = ")[1])

            value = value & fix_0
            value = value | fix_1

            mem[mem_address] = value


    print(sum(mem.values()))



def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")


    CURRENT_MASK = ""
    fix_0 = 0
    fix_1 = 0
    

    CURRENT_MASK_X_POSITIONS = []


    mem = {}
    for i in lines:
        if i.startswith("mask"):
            CURRENT_MASK = i.split(" = ")[1]

            fix_1 = int(CURRENT_MASK.replace("X", "0"), 2)

            fix_reset_all_but_1 = int(CURRENT_MASK.replace("0", "1").replace("X","0"),2)

            CURRENT_MASK_X_POSITIONS = [i for i,x in enumerate(reversed(list(CURRENT_MASK))) if x == "X"]

            print(CURRENT_MASK_X_POSITIONS)

        if i.startswith("mem"):
            print("NEW MEM LINE")
            print(i)
            base_mem_address = int(i.split("] =")[0].replace("mem[", ""))
            value = int(i.split(" = ")[1])


            # First fix the 1 in the mem-address 
            base_mem_address = (base_mem_address & fix_reset_all_but_1) | fix_1

            print(bin(base_mem_address))


            print("*****")            
            for c in range(2**len(CURRENT_MASK_X_POSITIONS)):
                foo = [int(y) for y in bin(c)[2:]]
                foo = (len(CURRENT_MASK_X_POSITIONS) - len(foo)) * [0] + foo
                print(foo)

                new_address = base_mem_address

                for _i, c2 in enumerate(CURRENT_MASK_X_POSITIONS):
                    new_address = new_address | foo[_i] * 2**c2 

                print(new_address)


                mem[new_address] = value

            print("*****")            






    print(sum(mem.values()))



if __name__ == "__main__":
    #part1("foo.txt")
    part1("inputs/day_14.txt")
    #part2("foo.txt")
    part2("inputs/day_14.txt")
