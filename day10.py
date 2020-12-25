import os
import itertools
import re
import collections


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")
 
    lines = [int(x) for x in lines]
  
    device_jolt = max(lines) + 3
  
    print(device_jolt)


    lines = [0] + sorted(lines) + [device_jolt]


    delta_1 = 0
    delta_3 = 0 
    for i in range(1, len(lines)):

        delta = lines[i] - lines[i-1]

        if delta == 3:
            delta_3 += 1

        if delta == 1:
            delta_1 += 1


    print(delta_1)
    print(delta_3)
    print(delta_1 * delta_3)


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")
 
    lines = [int(x) for x in lines]
  
    device_jolt = max(lines) + 3
  
    lines = [0] + sorted(lines) + [device_jolt]

    state = {lines[-2] : 1, lines[-3] : 1}
    for i in range(len(lines) - 4, -1, -1):
      combos = state[lines[i+1]] #You know the next adapter will fit
      if lines[i+3] - lines[i] <= 3:
        combos += state[lines[i+2]] + state[lines[i+3]]
      elif lines[i+2] - lines[i] <= 3:
        combos += state[lines[i+2]]
      state[lines[i]] = combos
    print(state[0])
    


if __name__ == "__main__":
    #part1("foo.txt")
    part1("inputs/day_10.txt")
    #part2("foo.txt")
    part2("inputs/day_10.txt")

