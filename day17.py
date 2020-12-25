import os
import copy
import itertools
import re
import collections
import math
import functools



def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip()


    directions = list(itertools.product( [-1,0,1], repeat=3))
    directions.remove( (0,0,0) )


    state = {}

    for (y,line) in enumerate(lines.split("\n")):
        for (x,cell) in enumerate(line):
            if cell == "#":
                state[ (x,y,0) ] = 1
            else:
                state[ (x,y,0) ] = 0



    for iteration in range(6):
        active_neighbours = {}


        # Broadcast my status to the neighbours
        for k,v in state.items():
            cell_x, cell_y, cell_z = k

            for dx,dy,dz in directions:
                active_neighbours[ (cell_x + dx, cell_y + dy, cell_z + dz) ] = active_neighbours.get( (cell_x + dx, cell_y + dy, cell_z + dz) , 0) + v
        print("hello")
        print(sum([v for k,v in active_neighbours.items() if k[2] == 0]))

        # Sum all information from neighbours
        new_state = {}
        foo = 0 
        for k,v in active_neighbours.items():
            cell_x, cell_y, cell_z = k

            current_cell_state = state.get(k,0)

            if current_cell_state == 1:
                if ( 2 <= v <= 3 ):
                    print(sum([v for k,v in new_state.items() if k[2] == 0]))
                    if cell_z == 0:
                        print(f"AAA {k}")
                        foo += 1
                    new_state[k] = 1
                    print(sum([v for k,v in new_state.items() if k[2] == 0]))
                else:
                    new_state[k] = 0

            #if cell_y == 2 and cell_z == 0:
            #    print(f"( {cell_x}, {cell_y} , {cell_z}) = {state.get(k,0)}    (active neighbours = {v})")

            if current_cell_state == 0:
                if v==3:
                    new_state[k] = 1
                else:
                    new_state[k] = 0


        state = copy.deepcopy(new_state)


     


    print( len( [k for k,v in state.items() if v == 1] ))


    print( sum(( [ (v) for k,v in state.items() ] )))



def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip()


    directions = list(itertools.product( [-1,0,1], repeat=4))
    directions.remove( (0,0,0,0) )


    state = {}

    for (y,line) in enumerate(lines.split("\n")):
        for (x,cell) in enumerate(line):
            if cell == "#":
                state[ (x,y,0, 0) ] = 1
            else:
                state[ (x,y,0, 0) ] = 0



    for iteration in range(6):
        active_neighbours = {}


        # Broadcast my status to the neighbours
        for k,v in state.items():
            cell_x, cell_y, cell_z, cell_w = k

            for dx,dy,dz, dw in directions:
                active_neighbours[ (cell_x + dx, cell_y + dy, cell_z + dz, cell_w + dw) ] = active_neighbours.get( (cell_x + dx, cell_y + dy, cell_z + dz, cell_w + dw) , 0) + v
        print("hello")
        print(sum([v for k,v in active_neighbours.items() if k[2] == 0]))

        # Sum all information from neighbours
        new_state = {}
        foo = 0 
        for k,v in active_neighbours.items():
            cell_x, cell_y, cell_z, cell_w = k

            current_cell_state = state.get(k,0)

            if current_cell_state == 1:
                if ( 2 <= v <= 3 ):
                    new_state[k] = 1
                else:
                    new_state[k] = 0

            #if cell_y == 2 and cell_z == 0:
            #    print(f"( {cell_x}, {cell_y} , {cell_z}) = {state.get(k,0)}    (active neighbours = {v})")

            if current_cell_state == 0:
                if v==3:
                    new_state[k] = 1
                else:
                    new_state[k] = 0


        state = copy.deepcopy(new_state)


        #if iteration >= 0:
        #    break

    print( len( [k for k,v in state.items() if v == 1] ))


    print( sum(( [ (v) for k,v in state.items() ] )))

if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_17.txt")
    #part2("foo.txt")
    part2("inputs/day_17.txt")
