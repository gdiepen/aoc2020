import os
import itertools
import re
import collections


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")
 

    # E / S / W / N
    DIRECTIONS = [ (1,0), (0, -1) , (-1,0),  (0,1) ]

    CURRENT_DIRECTION = 0

    CURRENT_X = 0 
    CURRENT_Y = 0 

    for x in lines:

        command = x[0]
        number = int(x[1:])


        if command == "N":
            CURRENT_Y += number 

        if command == "S":
            CURRENT_Y -= number 

        
        if command == "E":
            CURRENT_X += number 

        if command == "W":
            CURRENT_X -= number 

        if command == "F":
            CURRENT_X += DIRECTIONS[CURRENT_DIRECTION][0] * number
            CURRENT_Y += DIRECTIONS[CURRENT_DIRECTION][1] * number


        if command == "L":
            CURRENT_DIRECTION = (CURRENT_DIRECTION - (number//90) + 1024) % 4

        if command == "R":
            CURRENT_DIRECTION = (CURRENT_DIRECTION + (number//90) + 1024) % 4

    print(abs(CURRENT_X) + abs(CURRENT_Y))


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")
 

    # E / S / W / N
    DIRECTIONS = [ (1,0), (0, -1) , (-1,0),  (0,1) ]

    CURRENT_DIRECTION = 0

    SHIP_CURRENT_X = 0 
    SHIP_CURRENT_Y = 0 

    WAYPOINT_CURRENT_X = 10
    WAYPOINT_CURRENT_Y = 1

    for x in lines:
        command = x[0]
        number = int(x[1:])

        if command == "N":
            WAYPOINT_CURRENT_Y += number 

        if command == "S":
            WAYPOINT_CURRENT_Y -= number 

        
        if command == "E":
            WAYPOINT_CURRENT_X += number 

        if command == "W":
            WAYPOINT_CURRENT_X -= number 

        if command == "F":
            delta_x = WAYPOINT_CURRENT_X * number
            delta_y = WAYPOINT_CURRENT_Y * number

            # WAYPOINT_CURRENT_X += delta_x
            # WAYPOINT_CURRENT_X += delta_y

            SHIP_CURRENT_X += delta_x
            SHIP_CURRENT_Y += delta_y


        if command == "L":
            CURRENT_DIRECTION = (CURRENT_DIRECTION - (number//90) + 4) % 4

            num_rotations = number//90

            # delta_x = WAYPOINT_CURRENT_X - SHIP_CURRENT_X
            # delta_y = WAYPOINT_CURRENT_Y - SHIP_CURRENT_Y

            for i in range(num_rotations):
                foo_x = WAYPOINT_CURRENT_X
                foo_y = -WAYPOINT_CURRENT_Y

                WAYPOINT_CURRENT_X = foo_y
                WAYPOINT_CURRENT_Y = foo_x

            # WAYPOINT_CURRENT_X = SHIP_CURRENT_X + delta_x
            # WAYPOINT_CURRENT_Y = SHIP_CURRENT_Y + delta_y



        if command == "R":
            CURRENT_DIRECTION = (CURRENT_DIRECTION + (number//90) + 4) % 4

            num_rotations = number//90

            # delta_x = WAYPOINT_CURRENT_X - SHIP_CURRENT_X
            # delta_y = WAYPOINT_CURRENT_Y - SHIP_CURRENT_Y

            for i in range(num_rotations):
                foo_x = -WAYPOINT_CURRENT_X
                foo_y = WAYPOINT_CURRENT_Y

                WAYPOINT_CURRENT_X = foo_y
                WAYPOINT_CURRENT_Y = foo_x



        print()
        print(x)
        print(f"    WAYPOINT: {WAYPOINT_CURRENT_X}, {WAYPOINT_CURRENT_Y}")
        print(f"    SHIP: {SHIP_CURRENT_X}, {SHIP_CURRENT_Y}")

    print(abs(SHIP_CURRENT_X) + abs(SHIP_CURRENT_Y))



        

if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_12.txt")
    #part2("foo.txt")
    part2("inputs/day_12.txt")

