import os
import itertools


def do_calc(input_file, slope_x, slope_y):
    with open(input_file) as f:
        lines = f.read().split("\n")
    lines = [x for x in lines if x != ""]


    
    width = len(lines[0])
    height = len(lines)


    current_x = 0 
    current_y = 0 

    num_trees = 0
    while current_y < height:
        if lines[current_y][current_x] == "#":
            num_trees += 1

        current_x = (current_x + slope_x) % width
        current_y += slope_y

    return num_trees



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

def part2(input_file):

    results = []
    for i,j in [ (1,1) , (3,1), (5,1), (7,1), (1,2) ]:
        results.append( do_calc(input_file, i,j))

    result = 1
    print(results)
    for i in results:
        result = result * i

    print(result)



if __name__ == "__main__":
    part1("inputs/day_03.txt")
    part2("inputs/day_03.txt")

