import os
import copy
import itertools
import re
import collections
import math

def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")


    numbers = [int(x) for x in lines[0].split(",")]

    print(numbers)


    when_last_said = {}
    most_recent = -1

    for i in range(2020):
        if i < len(numbers):
            when_last_said[numbers[i]] = when_last_said.get(numbers[i], [])
            when_last_said[numbers[i]].append(i)

            most_recent = numbers[i]

        else:

            if (len(when_last_said[most_recent]) == 1) and (when_last_said[most_recent][0] == (i-1)):

                new_number = 0
                when_last_said[new_number] = when_last_said.get(new_number, [])
                when_last_said[new_number].append(i)
                
                most_recent = new_number
            else: 

                # Take the last two items from when it was last said
                t1, t2 = when_last_said[most_recent][-2:]

                new_number = t2 - t1
                when_last_said[new_number] = when_last_said.get(new_number, [])
                when_last_said[new_number].append(i)
                
                most_recent = new_number
        #print(most_recent) 




    #print (when_last_said)
    print(most_recent)


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")


    numbers = [int(x) for x in lines[0].split(",")]

    print(numbers)


    when_last_said = {}
    most_recent = -1

    for i in range(30000000):
        if i < len(numbers):
            when_last_said[numbers[i]] = when_last_said.get(numbers[i], [])
            when_last_said[numbers[i]].append(i)

            most_recent = numbers[i]

        else:

            if (len(when_last_said[most_recent]) == 1) and (when_last_said[most_recent][0] == (i-1)):

                new_number = 0
                when_last_said[new_number] = when_last_said.get(new_number, [])
                when_last_said[new_number].append(i)
                
                most_recent = new_number
            else: 

                # Take the last two items from when it was last said
                t1, t2 = when_last_said[most_recent][-2:]

                new_number = t2 - t1
                when_last_said[new_number] = when_last_said.get(new_number, [])
                when_last_said[new_number].append(i)
                
                most_recent = new_number
        #print(most_recent) 




    #print (when_last_said)
    print(most_recent)




if __name__ == "__main__":
    #part1("foo.txt")
    part1("inputs/day_15.txt")
    #part2("foo.txt")
    part2("inputs/day_15.txt")

