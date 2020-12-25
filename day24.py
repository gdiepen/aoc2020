
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

    black_tiles = {}

   
    # e => 0
    # se => 1
    # sw3 => 2
    # w => 3
    # nw => 4
    # ne => 5

    position_delta = {
        "0": (1,1),
        "1": (1,-1),
        "2": (0,-2),
        "3": (-1,-1),
        "4": (-1,1),
        "5": (0,2),

    }

    for line in lines.split("\n"):
        line = line.replace("se", "1")
        line = line.replace("sw", "2")
        line = line.replace("nw", "4")
        line = line.replace("ne", "5")
        line = line.replace("e", "0")
        line = line.replace("w", "3")

        print(line)
        cur_x = 0
        cur_y = 0 
        for instruction in list(line):
            cur_x = cur_x + position_delta[instruction][0]
            cur_y = cur_y + position_delta[instruction][1]
        
        if (cur_x, cur_y) in black_tiles:
            del black_tiles[(cur_x, cur_y)]
        else:
            black_tiles[(cur_x, cur_y)] = 1


    print(len(black_tiles.keys()))





def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip()

    black_tiles = {}

   
    # e => 0
    # se => 1
    # sw3 => 2
    # w => 3
    # nw => 4
    # ne => 5

    position_delta = {
        "0": (1,1),
        "1": (1,-1),
        "2": (0,-2),
        "3": (-1,-1),
        "4": (-1,1),
        "5": (0,2),

    }

    for line in lines.split("\n"):
        line = line.replace("se", "1")
        line = line.replace("sw", "2")
        line = line.replace("nw", "4")
        line = line.replace("ne", "5")
        line = line.replace("e", "0")
        line = line.replace("w", "3")

        print(line)
        cur_x = 0
        cur_y = 0 
        for instruction in list(line):
            cur_x = cur_x + position_delta[instruction][0]
            cur_y = cur_y + position_delta[instruction][1]
        
        if (cur_x, cur_y) in black_tiles:
            del black_tiles[(cur_x, cur_y)]
        else:
            black_tiles[(cur_x, cur_y)] = 1


    # Now that we have the tiles

    for day in range(100):

        black_neighbor_tile_count = collections.defaultdict(int)

        for black_tile in black_tiles.keys():

            black_tile_x, black_tile_y = black_tile


            for d_x, d_y in position_delta.values():
                black_neighbor_tile_count[ (black_tile_x + d_x , black_tile_y + d_y) ]  += 1

        new_black_tiles = {}

        for tile_xy, _count in black_neighbor_tile_count.items():

            # If it was a black tile
            if tile_xy in black_tiles.keys():
                # Stays black
                if 1 <=_count <= 2:
                    new_black_tiles[tile_xy] = 1

            else:
                # white that turns black
                if _count == 2:
                    new_black_tiles[tile_xy] = 1
        black_tiles = new_black_tiles

        print(f"day {day}: {len(black_tiles.keys())}")











if __name__ == "__main__":
    #part1("foo.txt")
    part1("inputs/day_24.txt")
    #part2("foo.txt")
    part2("inputs/day_24.txt")


