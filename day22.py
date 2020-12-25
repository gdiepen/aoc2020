
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

    player_decks = [] 
    players = []

    for block in lines.split("\n\n"):

        player_name = block.split("\n")[0]
        player_deck = [int(x) for x in block.split("\n")[1:]]

        players.append(player_name)
        player_decks.append(player_deck)


    finished = False

    print(player_decks)

    while not finished:

        for i,k in enumerate(player_decks):
            print(f"Player {i} : {k}")

        round_cards = {x: player_decks[x].pop(0) for x in range(len(players))}


        _winning = sorted( round_cards.items() , key=lambda x: -x[1])

        print(_winning)

        _winner = _winning[0][0]

        
        print(f"Player {_winner} wins the round")

        _winning_card = _winning[0][1]

        remaining_cards = [x[1] for x in _winning[1:]]


        player_decks[_winner].extend([_winning_card])
        player_decks[_winner].extend(remaining_cards)


        for k in player_decks:
            if len(k) == 0:
                finished = True


    for p in player_decks:
        if len(p) > 0:
            total_score = 0 
            for i,k in enumerate(p):
                total_score += (len(p) - i )  * k


            print(total_score)



all_seen_combinations_deck1 = collections.defaultdict(dict)
all_seen_combinations_deck2 = collections.defaultdict(dict)


def calc_score(deck):
    total_score = 0 
    for i,k in enumerate(deck):
        total_score += (len(deck) - i )  * k


    return total_score



def play_game(game_level, deck1, deck2):

    finished = False

    iteration = 0 
    while not finished:
        iteration += 1

        if tuple(deck1) in all_seen_combinations_deck1[game_level].keys():
            return 1, deck1, deck2

        if tuple(deck2) in all_seen_combinations_deck2[game_level].keys():
            return 1, deck1, deck2


        all_seen_combinations_deck1[game_level][ tuple(deck1) ] = 1
        all_seen_combinations_deck2[game_level][ tuple(deck2) ] = 1



        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        print(f"Game level {game_level} , iteration {iteration}")
        print(f"    [{card1}]   {deck1}")
        print(f"    [{card2}]   {deck2}")

        if (card1 <= len(deck1)) and (card2 <= len(deck2)):
            print(" Recursing...")
            # Recursive:

            all_seen_combinations_deck1[game_level + 1] = {}
            all_seen_combinations_deck2[game_level + 1] = {}

            winner_subgame, _, _ = play_game(game_level + 1, [x for x in deck1][:card1], [x for x in deck2][:card2])

            print(f"Winner of recursed game at level {game_level} is {winner_subgame}")

            if winner_subgame == 1:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])
        else:
            if card1 > card2:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])

        if len(deck1) == 0:
            return 2, deck1, deck2
        if len(deck2) == 0:
            return 1, deck1, deck2




def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip()

    player1_deck = [int(x) for x in lines.split("\n\n")[0].split("\n")[1:]]
    player2_deck = [int(x) for x in lines.split("\n\n")[1].split("\n")[1:]]


    winner, deck1, deck2 = play_game(1, player1_deck, player2_deck)

    if winner == 1:
        print(calc_score(deck1))
    else:
        print(calc_score(deck2))









if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_22.txt")
    #part2("foo.txt")
    part2("inputs/day_22.txt")




