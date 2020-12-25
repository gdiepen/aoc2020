import os
import copy
import itertools
import re
import collections
import math
import functools

def get_corners(input_file):
    with open(input_file) as f:
        lines = f.read().strip()


    tile_blocks = lines.split("\n\n")

    side_numbers = collections.defaultdict(list)


    tiles = {}
    for t in tile_blocks:
        tile_number = re.findall(r"Tile (\d+):", t.split("\n")[0])[0]


        tile_data = t.split("\n")[1:]

        # Get number representing top:
        top_number = int(tile_data[0].replace(".", "0").replace("#", "1"), 2)
        top_number_rev = int(tile_data[0].replace(".", "0").replace("#", "1")[-1::-1], 2)




        # Get number representing left:
        left_number = int( "".join([ x[0] for x in tile_data ]).replace(".", "0").replace("#", "1"), 2)
        left_number_rev = int( "".join([ x[0] for x in tile_data ]).replace(".", "0").replace("#", "1")[-1::-1], 2)





        
        # Get number representing bottom:
        bottom_number = int(tile_data[-1].replace(".", "0").replace("#", "1"), 2)
        bottom_number_rev = int(tile_data[-1].replace(".", "0").replace("#", "1")[-1::-1], 2)

        # Get number representing left:
        right_number = int( "".join([ x[-1] for x in tile_data ]).replace(".", "0").replace("#", "1"), 2)
        right_number_rev = int( "".join([ x[-1] for x in tile_data ]).replace(".", "0").replace("#", "1")[-1::-1], 2)


         
        side_numbers[top_number].append(tile_number)
        side_numbers[top_number_rev].append(tile_number)

        side_numbers[bottom_number].append(tile_number)
        side_numbers[bottom_number_rev].append(tile_number)

        side_numbers[left_number].append(tile_number)
        side_numbers[left_number_rev].append(tile_number)

        side_numbers[right_number].append(tile_number)
        side_numbers[right_number_rev].append(tile_number)



    # Delete all the ones that have no match
    to_delete = [k for k,v in side_numbers.items() if len(v) == 1]

    for d in to_delete:
        del side_numbers[d]

    c = collections.Counter(itertools.chain(*side_numbers.values()))

    print(c.most_common()[-4:])
    print(functools.reduce( lambda x,y: x*y,   [int(tile_id) for tile_id, _ in c.most_common()[-4:]]))

    return [x[0] for x in c.most_common()][-4:]


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip()


    tile_blocks = lines.split("\n\n")

    side_numbers = collections.defaultdict(list)


    tiles = {}
    for t in tile_blocks:
        tile_number = re.findall(r"Tile (\d+):", t.split("\n")[0])[0]


        tile_data = t.split("\n")[1:]

        # Get number representing top:
        top_number = int(tile_data[0].replace(".", "0").replace("#", "1"), 2)
        top_number_rev = int(tile_data[0].replace(".", "0").replace("#", "1")[-1::-1], 2)




        # Get number representing left:
        left_number = int( "".join([ x[0] for x in tile_data ]).replace(".", "0").replace("#", "1"), 2)
        left_number_rev = int( "".join([ x[0] for x in tile_data ]).replace(".", "0").replace("#", "1")[-1::-1], 2)





        
        # Get number representing bottom:
        bottom_number = int(tile_data[-1].replace(".", "0").replace("#", "1"), 2)
        bottom_number_rev = int(tile_data[-1].replace(".", "0").replace("#", "1")[-1::-1], 2)

        # Get number representing left:
        right_number = int( "".join([ x[-1] for x in tile_data ]).replace(".", "0").replace("#", "1"), 2)
        right_number_rev = int( "".join([ x[-1] for x in tile_data ]).replace(".", "0").replace("#", "1")[-1::-1], 2)


         
        side_numbers[top_number].append(tile_number)
        side_numbers[top_number_rev].append(tile_number)

        side_numbers[bottom_number].append(tile_number)
        side_numbers[bottom_number_rev].append(tile_number)

        side_numbers[left_number].append(tile_number)
        side_numbers[left_number_rev].append(tile_number)

        side_numbers[right_number].append(tile_number)
        side_numbers[right_number_rev].append(tile_number)



    # Delete all the ones that have no match
    to_delete = [k for k,v in side_numbers.items() if len(v) == 1]

    for d in to_delete:
        del side_numbers[d]

    c = collections.Counter(itertools.chain(*side_numbers.values()))

    print(c.most_common()[-4:])
    print(functools.reduce( lambda x,y: x*y,   [int(tile_id) for tile_id, _ in c.most_common()[-4:]]))


class TileData:

    def __init__(self, tile_number, tile_data, orientation=0, flipped_horizontal=False, flipped_vertical=False):
        self.tile_data = tile_data
        self.cleaned_tile_data = [x[1:-1] for x in tile_data[1:-1]]

        self.orientation = orientation
        self.flipped_vertical = flipped_vertical
        self.flipped_horizontal = flipped_horizontal
        self.side_num = {}
        self.side_num["top"] = int(tile_data[0].replace(".", "0").replace("#", "1"), 2)
        self.side_num["bottom"] = int(tile_data[-1].replace(".", "0").replace("#", "1"), 2)
        self.side_num["left"] = int( "".join([ x[0] for x in tile_data ]).replace(".", "0").replace("#", "1"), 2)
        self.side_num["right"] = int( "".join([ x[-1] for x in tile_data ]).replace(".", "0").replace("#", "1"), 2)

        self.tile_number = tile_number


    def __hash__(self):
        #foo = []

        #for k,v in self.side_num.items():
        #    foo.append( (k,v,))

        #foo.append(self.tile_number)

        #return hash(tuple(foo))
        return hash(self.__str__())


    def __eq__(self, other):
        if not isinstance(other, TileData):
            return NotImplemented

        foo = [self.side_num[x] == other.side_num[x] for x in self.side_num.keys()]

        return (self.tile_number == other.tile_number) and all(foo)

    def __str__(self):
        return f"<Tile number={self.tile_number}  top={self.side_num['top']}  right={self.side_num['right']}  bottom={self.side_num['bottom']}  left={self.side_num['left']}, flipped_horizontal={self.flipped_horizontal}  flipped_vertical={self.flipped_vertical}  orientation={self.orientation}  >"

def flip_tile_horizontal(tile):
    result = [x[-1::-1] for x in tile]
    return result

def flip_tile_vertical(tile):
    result = [x for x in tile[-1::-1]]
    return result

def rotate_tile_cw(tile):
    tile = [list(x) for x in tile]

    result = [[tile[j][i] for j in range(len(tile))] for i in range(len(tile[0])-1,-1,-1)]
    result = [ "".join(x) for x in result ]
    return result

def check_for_monsters(poster_data):

    ## 0                  # 
    ## 1#    ##    ##    ###
    ## 2 #  #  #  #  #  #   
    ##  01234567890123456789

    sea_monster = [ (0,1) , (1,2) , (4,2), (5,1), (6,1) , (7,2), (10,2), (11,1), (12,1), (13,2), (16,2), (17,1), (18,1), (19,1), (18,0) ] 

    total_num_hash = 0
    for i in poster_data:
        total_num_hash += sum( [1 for x in i if x == "#"])

    num_sea_monsters = 0
    for x in range(len(poster_data) - 19):
        for y in range(len(poster_data[0]) - 3):

            chars = [poster_data[y + e_y][ x + e_x] for (e_x, e_y) in sea_monster]

            num_hash = sum( [1 for c in chars if c == "#"])

            if num_hash == len(sea_monster):
                num_sea_monsters += 1
    if num_sea_monsters > 0:
        print(num_sea_monsters)
        print(total_num_hash - num_sea_monsters * len(sea_monster))



def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip()


    tile_blocks = lines.split("\n\n")

    all_tiles_all_posititions = []
    for t in tile_blocks:
        tile_number = re.findall(r"Tile (\d+):", t.split("\n")[0])[0]


        tile_data = t.split("\n")[1:]

        _tile = TileData(tile_number, tile_data, 0, False, False)
        all_tiles_all_posititions.append(_tile)


        _tile = TileData(tile_number, (flip_tile_vertical(tile_data)), 0, False, True)
        all_tiles_all_posititions.append(_tile)

        _tile = TileData(tile_number, (flip_tile_horizontal(tile_data)), 0, True, False)
        all_tiles_all_posititions.append(_tile)

        _tile = TileData(tile_number, (flip_tile_vertical(flip_tile_horizontal(tile_data))), 0, True, True)
        all_tiles_all_posititions.append(_tile)



        _tile_data = tile_data
        for i in range(1,4):
            _tile_data = rotate_tile_cw(_tile_data)

            _tile = TileData(tile_number, _tile_data, i, False, False)
            all_tiles_all_posititions.append(_tile)

            _tile = TileData(tile_number, (flip_tile_vertical(_tile_data)), i, False, True)
            all_tiles_all_posititions.append(_tile)

            _tile = TileData(tile_number, (flip_tile_horizontal(_tile_data)), i, True, False)
            all_tiles_all_posititions.append(_tile)

            _tile = TileData(tile_number, (flip_tile_vertical(flip_tile_horizontal(_tile_data))), i, True, True)
            all_tiles_all_posititions.append(_tile)


    
    #all_tiles_all_posititions = list(set((all_tiles_all_posititions)))


    placed_tiles = {}
    


    corner_points = get_corners(input_file)
    print(corner_points)


    # we know that one of the corner points must be correct

    possible_starting_tiles = [x for x in all_tiles_all_posititions if x.tile_number == corner_points[0]]

    print("number of tests:")
    print(len(possible_starting_tiles))


    for i in range(len(possible_starting_tiles)):

        print(f"Starting with element {i}")


        # now take one tile
        # initial_tile = remaining_tiles.pop(i)
        initial_tile = possible_starting_tiles[i]


        remaining_tiles = [x for x in all_tiles_all_posititions if x.tile_number != initial_tile.tile_number ]



        # place it
        placed_tiles = {}
        placed_tiles[ (0,0) ] = initial_tile

        open_sides = {}
        for s in ["top", "bottom" , "left", "right"]:
            open_sides[ (0,0, s) ] = initial_tile.side_num[s]

        # print(f"Placed tile {initial_tile.tile_number} at (0,0)")
        # print(initial_tile)



        # And remove this complete tile number from the list of tiles
        remaining_tiles = [x for x in remaining_tiles if x.tile_number != initial_tile.tile_number]
        
        opposite={"top": "bottom", "bottom": "top" , "left": "right" , "right": "left"}

        new_position = {"top": (0,1), "bottom": (0,-1), "left": (-1,0), "right": (1,0)}

        finished = False
        while not finished:
            # Try to find anything that matches the open_sides

            placed_tile = False
            for open_side, open_side_num in open_sides.items():
                open_side_x, open_side_y, open_side_side = open_side
                # print(f"Side {open_side_side} = {open_side_num}")

                # Check if there are any open sides that match
                matching_side_tiles = [x for x in remaining_tiles if x.side_num[ opposite[open_side_side] ] == open_side_num]

                if len(matching_side_tiles) > 0:
                    _matched_tile = matching_side_tiles[0]

                    new_x = open_side_x + new_position[open_side_side][0]
                    new_y = open_side_y + new_position[open_side_side][1]



                    placed_tiles[ (new_x, new_y) ] = _matched_tile


                    #print(f"Start {i} :: Placing tile {_matched_tile.tile_number} at ({new_x}, {new_y})")
                    placed_tile = True

                    for s in ["top", "bottom" , "left", "right"]:
                        if (new_x, new_y,s) not in open_sides.keys():
                            open_sides[ (new_x,new_y, s) ] = _matched_tile.side_num[s]
                    
                    open_sides[open_side] = -1

                    remaining_tiles = [x for x in remaining_tiles if x.tile_number != _matched_tile.tile_number]


                    break
            if len(remaining_tiles) == 0:
                finished = True
            # or if we are hanging, also finished
            if not placed_tile:
                finished = True

        if len(remaining_tiles) == 0:

            print("FOUND SOLUTION!!")
            break
        else:
            print(f"    number of remaining tiles = {len(remaining_tiles)}")
            placed_tiles = {}

    if len(placed_tiles.keys()):

        for k,v in placed_tiles.items():
            print(f"    at {k} place tile {v.tile_number}")


        min_x = min([x[0] for x in placed_tiles.keys()])
        max_x = max([x[0] for x in placed_tiles.keys()])

        min_y = min([x[1] for x in placed_tiles.keys()])
        max_y = max([x[1] for x in placed_tiles.keys()])



        for y in reversed(range( min_y, max_y+1)):
            print(f"Line {y}:")
            for x in (range(min_x, max_x+1)):

                print(f"    {placed_tiles[(x,y)]}")






        poster_lines = []
        # Now start creating the tile data
        for y in reversed(range( min_y, max_y+1)):

            current_block_row = [  placed_tiles[(x,y)].cleaned_tile_data for x in range(min_x, max_x + 1)  ]


            num_rows_in_tile = len(current_block_row[0])


            for i in range(num_rows_in_tile):
                poster_line = "".join([ x[i] for x in current_block_row])
                poster_lines.append(poster_line)

        
            
        print("\n".join(poster_lines))


        poster_data = [x for x in poster_lines]


        check_for_monsters(poster_data)
        check_for_monsters(flip_tile_vertical(poster_data))
        check_for_monsters(flip_tile_horizontal(poster_data))
        check_for_monsters(flip_tile_vertical(flip_tile_horizontal(poster_data)))

        #print()
        #print()
        #print()
        #print("\n".join(flip_tile_vertical(rotate_tile_cw(rotate_tile_cw(rotate_tile_cw(poster_data))))))
        #check_for_monsters((rotate_tile_cw(rotate_tile_cw(rotate_tile_cw(poster_data)))))






        for i in range(3):

            poster_data = rotate_tile_cw(poster_data)

            check_for_monsters(poster_data)
            check_for_monsters(flip_tile_vertical(poster_data))
            check_for_monsters(flip_tile_horizontal(poster_data))
            check_for_monsters(flip_tile_vertical(flip_tile_horizontal(poster_data)))





if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_20.txt")
    #part2("foo.txt")
    part2("inputs/day_20.txt")
