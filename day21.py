
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


    foods = lines.split("\n")


    all_ingredients = []
    all_allergens = []
    for food in foods:
        ingredients = food.split(" (contains ")[0].split(" ")
        allergens = food.split(" (contains ")[1].replace(")", "").split(", ")

        all_ingredients.extend(ingredients)
        all_allergens.extend(allergens)

    all_ingredients = list(set(all_ingredients))
    all_allergens = list(set(all_allergens))


    #potential_allergens = { x:all_allergens for x in all_ingredients }
    #potential_allergens = { x:all_ingredients for x in all_ingredients }

    ingredient_occurrences = {x:0 for x in all_ingredients}
    allergen_occurrences = {x:0 for x in all_allergens}


    potential_ingredients_for_allergen = { x:all_ingredients for x in all_allergens}
    potential_allergens_for_ingredient = { x:[] for x in all_ingredients}



    combinations = collections.defaultdict(int)


    for food in foods:
        ingredients = food.split(" (contains ")[0].split(" ")
        allergens = food.split(" (contains ")[1].replace(")", "").split(", ")



        for a in allergens:
            allergen_occurrences[a] += 1
            potential_ingredients_for_allergen[a] = [x for x in potential_ingredients_for_allergen[a] if x in ingredients]

        for i in ingredients:
            ingredient_occurrences[i] += 1




    import pprint

    print("Potential ingredients for each allergen")
    pprint.pprint(potential_ingredients_for_allergen)

    print("Number of ingredient occurrences")
    pprint.pprint(ingredient_occurrences)

    result = 0 
    for i in all_ingredients:
        if i not in itertools.chain(*potential_ingredients_for_allergen.values()):
            result += ingredient_occurrences[i]

    print(result)




def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip()


    foods = lines.split("\n")


    all_ingredients = []
    all_allergens = []
    for food in foods:
        ingredients = food.split(" (contains ")[0].split(" ")
        allergens = food.split(" (contains ")[1].replace(")", "").split(", ")

        all_ingredients.extend(ingredients)
        all_allergens.extend(allergens)

    all_ingredients = list(set(all_ingredients))
    all_allergens = list(set(all_allergens))


    #potential_allergens = { x:all_allergens for x in all_ingredients }
    #potential_allergens = { x:all_ingredients for x in all_ingredients }

    ingredient_occurrences = {x:0 for x in all_ingredients}
    allergen_occurrences = {x:0 for x in all_allergens}


    potential_ingredients_for_allergen = { x:all_ingredients for x in all_allergens}
    potential_allergens_for_ingredient = { x:[] for x in all_ingredients}



    combinations = collections.defaultdict(int)


    for food in foods:
        ingredients = food.split(" (contains ")[0].split(" ")
        allergens = food.split(" (contains ")[1].replace(")", "").split(", ")



        for a in allergens:
            allergen_occurrences[a] += 1
            potential_ingredients_for_allergen[a] = [x for x in potential_ingredients_for_allergen[a] if x in ingredients]

        for i in ingredients:
            ingredient_occurrences[i] += 1




    import pprint

    print("Potential ingredients for each allergen")
    pprint.pprint(potential_ingredients_for_allergen)

    print("Number of ingredient occurrences")
    pprint.pprint(ingredient_occurrences)


    print()
    print()
    print()
    print()
    print("Removing options")
    allergen_mapping = {}

    finished = False
    while not finished:
        # Does there exist a allergen with just one ingredient?
        result = [ (k,v) for k,v in potential_ingredients_for_allergen.items() if len(v) == 1]


        if len(result) > 0:
            _allergen = result[0][0]
            _ingredient = result[0][1][0]


            print(f"Allergen {_allergen}  :: Ingredient {_ingredient}")

            allergen_mapping[_ingredient] = _allergen

            # now delete this allergen

            del potential_ingredients_for_allergen[_allergen]
            # And remove the ingredient from all of the other ones

            for k2,v2 in potential_ingredients_for_allergen.items():
                if _ingredient in v2:
                    v2.remove(_ingredient)

            pprint.pprint(potential_ingredients_for_allergen)



        if len(result) == 0:
            print("Shit")
            finished = True


        if len(potential_ingredients_for_allergen.keys()) == 0:
            finished = True
        

    import pprint
    pprint.pprint(allergen_mapping)

    result = allergen_mapping.items()

    result = ",".join([i[0] for i in sorted(result, key=lambda x:x[1])])

    print(result)

if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_21.txt")
    #part2("foo.txt")
    part2("inputs/day_21.txt")



