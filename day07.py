
import os
import itertools
import re
import collections


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")
   

    mapping = {}


    for x in lines:
        
        source_bag = re.match(r"^(\w+ \w+) bags contain", x).groups()[0]

       
        mapping[source_bag] = re.findall(r"(\d+) (\w+ \w+) bag", x)



    my_sum = 0 
    for bag_color in mapping.keys():

        can_hold_shiny_gold = False


        to_add = [bag_color]

        while len(to_add) > 0:
            _bag = to_add.pop(0)

            to_add.extend( [x for _, x in  mapping[_bag]] )

            if "shiny gold" in to_add:
                can_hold_shiny_gold = True

            
        if can_hold_shiny_gold:
            my_sum += 1

    print(my_sum)
      


def get_num_bags(mapping, bag_color):
    return 1 + sum([ num*get_num_bags(mapping, bag) for num,bag in mapping[bag_color]])

def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")
    mapping = {}


    for x in lines:
        
        source_bag = re.match(r"^(\w+ \w+) bags contain", x).groups()[0]

       
        mapping[source_bag] = [(int(x), y) for x, y in re.findall(r"(\d+) (\w+ \w+) bag", x)]


    

    print(get_num_bags(mapping, "shiny gold") - 1)



if __name__ == "__main__":
    part1("inputs/day_07.txt")
    part2("inputs/day_07.txt")

