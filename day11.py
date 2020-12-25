import os
import copy
import itertools
import re
import collections

def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    _org_width = len(lines[0])
    
    width = _org_width
    height = len(lines)


    lines = [" " + x + " " for x in lines]

    lines.insert(0,  (_org_width + 2)* " ")
    lines.append( (_org_width + 2)* " ")


    lines = [list(x) for x in lines]


    finished = False

    prev = ""

    while not finished:
        finished = True



        lines_new = copy.deepcopy(lines)


        for i,j in itertools.product( range(1, height+1), range(1, width+1) ):

            if lines[i][j] == ".":
                lines_new[i][j] = "."


            
            surrounding_seats = lines[i-1][j-1:j+2] + [lines[i][j-1]] + [lines[i][j+1]] + lines[i+1][j-1:j+2] 

            lines_new[i][j] = lines[i][j]

            lines_new[i][j] = lines[i][j]

            if lines[i][j] == "L":
                if sum([1 for x in surrounding_seats if x == "#"]) == 0:
                    lines_new[i][j] = "#"

            if lines[i][j] == "#":
                if sum([1 for x in surrounding_seats if x == "#"]) >= 4:
                    lines_new[i][j] = "L"

        lines = lines_new

        _current_state = "".join(["".join(x) for x in lines])
        
        if _current_state != prev:
            finished = False

            prev = _current_state

        else:
            print(sum([1 for x in  list(_current_state) if x == "#"]))
   



def count_occupied2(r, c, grid, rows, cols, deltas):
    count=0
    for i,j in deltas:
        xi,xj=r+i,c+j
        while 0<=xi<rows and 0<=xj<cols:
            if grid[xi][xj]=='#':
                count+=1
                break
            elif grid[xi][xj] == 'L':
                break
            xi+=i
            xj+=j
    return count

def check_occupied2(lines, thresh = 5):
    rows, cols = len(lines), len(lines[0])
    deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    while True:
        valid = True
        temp_grid=[r.copy() for r in lines]
        for i, r in enumerate(temp_grid):
            for j, c in enumerate(r):
                count = count_occupied2(i, j, temp_grid, rows,cols, deltas)
                if c=='L' and count==0:
                    lines[i][j]='#'
                elif c=='#' and count>=thresh:
                    lines[i][j]='L'
                valid&=(r[j]==lines[i][j])
        if valid:
            break
    ans=0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j]=='#':
                ans+=1
    print(f"There are {ans} valid seats.")


def part2(input_file):
    with open(input_file, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        lines = [list(line) for line in lines]


    check_occupied2(lines)

  


if __name__ == "__main__":
    part1("foo.txt")
    #part1("inputs/day_11.txt")
    #part2("foo.txt")
    part2("inputs/day_11.txt")
