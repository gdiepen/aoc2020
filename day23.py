
import os
import copy
import itertools
import re
import collections
import math
import functools



def part1(input_file):
    cups = [int(x) for x in list(input_file)]

    num_cups = len(cups)
    min_value = min(cups)
    print(min_value)
    max_value = max(cups)

    print(f"CUPS: {cups}")
    for i in range(100):
        print()
        print()
        print()
        print()

        print(f"Round {i}")
        num_to_pickup = 3
        print(f"  Number to pickup = {num_to_pickup}")

        cups = 2*cups

        print(f"     cups: {cups}")

        picked_up_cups = cups[1: 1 + num_to_pickup]
        print(f"  picked up cups: {picked_up_cups}")
        cups = [cups[0]] + cups[1 + num_to_pickup:]

        print(f"  remaining cups on table: {cups}")



        destination_cup = cups[0] - 1
        print(f"  destination cup {destination_cup}")

        if destination_cup < min_value:
            destination_cup = max_value
        while destination_cup in picked_up_cups:
            destination_cup -= 1
            if destination_cup < min_value:
                destination_cup = max_value
        print(f"  destination cup cleand {destination_cup}")

        # Now find the position after which we have to put the list

        index_to_insert = cups.index(destination_cup) 
        print(f"  index of cup {destination_cup} is  {index_to_insert}")

        cups = cups[:index_to_insert+1]  + picked_up_cups + cups[index_to_insert+1:]
        cups = cups[1:]
        cups = cups[:num_cups]

        print(f"  new cups: {cups}")


    cups = cups*2
    start_index = cups.index(1) + 1
    
    result = ""
    for i in range(num_cups - 1):
        result += str(cups[start_index + i])

    print(result)


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

def get_list(current_node):
    start_value = current_node.value

    result = f"({current_node.value})"

    current_node = current_node.next_node
    while current_node.value != start_value:
        result += f" {current_node.value}"
        current_node = current_node.next_node

    return result
    




def part2(input_file):
    cups = [int(x) for x in list(input_file)]

    max_value = max(cups)

    cups =  cups + list(range(max_value + 1, 1000000))

    while len(cups) < 1000000:
        cups = cups + [max(cups) + 1]



    node_list = [Node(i) for i in cups]
    for i in range(len(node_list)-1):
        node_list[i].next_node = node_list[i+1]

    node_list[-1].next_node = node_list[0]


    # Create lookup table
    node_dict = {}
    for n in node_list:
        node_dict[n.value] = n



    min_value = min(cups)
    max_value = max(cups)


    current_node = node_list[0]

    for game_round in range(10000000):

        if (game_round %  100000) == 0:
            print(game_round)

        destination_cup = current_node.value - 1

        pickup_cups = []


        beginning_of_cups_to_move = current_node.next_node

        end_of_cups_to_move = beginning_of_cups_to_move
        pickup_cups.append(end_of_cups_to_move.value)

        end_of_cups_to_move = end_of_cups_to_move.next_node
        pickup_cups.append(end_of_cups_to_move.value)

        end_of_cups_to_move = end_of_cups_to_move.next_node
        pickup_cups.append(end_of_cups_to_move.value)
        
        # Set the  next node because we took everything out
        current_node.next_node = end_of_cups_to_move.next_node



        if destination_cup < min_value:
            destination_cup = max_value
        while destination_cup in pickup_cups:
            destination_cup -= 1
            if destination_cup < min_value:
                destination_cup = max_value


        destination_cup_finder = node_dict[destination_cup]

        # Now update the end_of_cups_to_move
        end_of_cups_to_move.next_node = destination_cup_finder.next_node
        destination_cup_finder.next_node = beginning_of_cups_to_move


        current_node = current_node.next_node


    # Get the node for 1
    node_1 = [x for x in node_list if x.value == 1][0]

    first_value = node_1.next_node.value
    second_value = node_1.next_node.next_node.value

    print(first_value * second_value)









    

if __name__ == "__main__":
    #part1("389125467")
    part1("942387615")
    #part2("foo.txt")
    #part2("inputs/day_23.txt")
    #part2("389125467")
    part2("942387615")




