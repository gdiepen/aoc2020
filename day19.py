
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


    lines_rules = lines.split("\n\n")[0].split("\n")
    lines_input = lines.split("\n\n")[1].split("\n")


    rules = {}

    for i in lines_rules:
        
        rule_number = i.split(": ")[0]
        rule_content = " " + i.split(": ")[1].replace(" ", "  ") + " "


        rules[rule_number] = rule_content

    # Now build up the rule 0 string

    current_rule = rules["0"]

    foo = re.findall(r" (\d+) ", current_rule)
    while foo:

        for f in foo:
            current_rule = current_rule.replace(f" {f} ", "(" + rules[f]+")")

        foo = re.findall(r" (\d+) ", current_rule)

    current_rule  = current_rule.replace(" ", "")
    current_rule  = current_rule.replace("\"", "")
   
    current_rule = "^" + current_rule + "$"
    print(current_rule)

    current_rule = re.sub(r"\(([ab])\)", r"\1", current_rule)
    print(current_rule)



    total_match = 0 
    for line in lines_input:
        
        if re.match(current_rule, line):
            total_match += 1

    print(total_match)


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip()


    lines_rules = lines.split("\n\n")[0].split("\n")
    lines_input = lines.split("\n\n")[1].split("\n")


    rules = {}

    for i in lines_rules:
        
        rule_number = i.split(": ")[0]
        rule_content = " " + i.split(": ")[1].replace(" ", "  ") + " "


        rules[rule_number] = rule_content

    # Now build up the rule 0 string

    rules["8"] = " 42  +  "


    rules["11"] = " 42  __N__  31  __N__ "



    current_rule = rules["0"]

    foo = re.findall(r" (\d+) ", current_rule)
    while foo:

        for f in foo:
            current_rule = current_rule.replace(f" {f} ", "(" + rules[f]+")")

        foo = re.findall(r" (\d+) ", current_rule)

    current_rule  = current_rule.replace(" ", "")
    current_rule  = current_rule.replace("\"", "")
   
    current_rule = "^" + current_rule + "$"
    print(current_rule)


    current_rule = re.sub(r"\(([ab])\)", r"\1", current_rule)
    print(current_rule)


    matches = {}

    for i in range(1,10):

        _rule = current_rule.replace("__N__", "{" + str(i) + "}")


        total_match = 0 
        for line in lines_input:
            
            if re.match(_rule, line):
                total_match += 1

                matches[line] = True

        print(total_match)


    print(len(matches.keys()))


if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_19.txt")
    #part2("foo.txt")
    part2("inputs/day_19.txt")

