
import os
import copy
import itertools
import re
import collections
import math
import functools



def part1():
    #with open(input_file) as f:
    #    lines = f.read().strip()


    card_public_key = 7573546
    door_public_key = 17786549

    #card_public_key = 5764801
    #door_public_key = 17807724

    card_private_key = 0 

    calc_value = 1 
    subject_number = 7

    while calc_value != card_public_key:
        card_private_key += 1

        calc_value = calc_value * subject_number
        calc_value = calc_value % 20201227
    print(card_private_key)

    calc_value = 1 
    subject_number = 7
    door_private_key = 0 
    while calc_value != door_public_key:
        door_private_key += 1

        calc_value = calc_value * subject_number
        calc_value = calc_value % 20201227

    print(door_private_key)


    calc_value = 1
    subject_number = card_public_key
    
    # Now use the public key of the card with the private key  of the door
    for i in range(door_private_key):
        calc_value = calc_value * subject_number
        calc_value = calc_value % 20201227

    print(calc_value)





if __name__ == "__main__":
    #part1("foo.txt")
    part1()
    #part2("foo.txt")
    #part2("inputs/day_25.txt")


