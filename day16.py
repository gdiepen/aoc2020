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


    lines_requirements = lines.split("\n\n")[0].split("\n")
    you_ticket = lines.split("\n\n")[1]
    lines_nearby_tickets = lines.split("\n\n")[2].split("\n")[1:]



    requirements = {}

    for x in lines_requirements:
        _req_type = re.findall(r"(.*): ", x)[0]
        #foo = re.findall(r"(.*): ((\d+)-(\d+))( (\d+)-(\d+))*", x.replace(" or ", " "))[0]
        foo = re.findall(r"(\d+)-(\d+)", x.replace(" or ", " "))
        #foo = re.findall(r"(.*): (\d+-\d+)( \d+-\d+)*", x.replace(" or ", " "))


        foo = [(int(x1), int(x2)) for x1,x2 in foo]


        requirements[_req_type] = requirements.get(_req_type, [])
        requirements[_req_type].extend(foo)



    all_reqs = []

    for i in requirements.values():
        all_reqs.extend(i)


    sum_invalid = 0
    for x in lines_nearby_tickets:

        for x2 in x.split(","):
            x2 = int(x2)

            satisfy_req = [ (r_min <= x2 <= r_max) for r_min, r_max in all_reqs]

            if not any(satisfy_req):
                #print(f"    {x2}  is invalid")
                sum_invalid += x2


    print(sum_invalid)


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip()


    lines_requirements = lines.split("\n\n")[0].split("\n")
    you_ticket = lines.split("\n\n")[1]
    your_ticket_values = [int(x) for x in you_ticket.split("\n")[1].split(",")]
    lines_nearby_tickets = lines.split("\n\n")[2].split("\n")[1:]



    requirements = {}

    for x in lines_requirements:
        _req_type = re.findall(r"(.*): ", x)[0]
        #foo = re.findall(r"(.*): ((\d+)-(\d+))( (\d+)-(\d+))*", x.replace(" or ", " "))[0]
        foo = re.findall(r"(\d+)-(\d+)", x.replace(" or ", " "))
        #foo = re.findall(r"(.*): (\d+-\d+)( \d+-\d+)*", x.replace(" or ", " "))


        foo = [(int(x1), int(x2)) for x1,x2 in foo]


        requirements[_req_type] = requirements.get(_req_type, [])
        requirements[_req_type].extend(foo)



    all_reqs = []

    for i in requirements.values():
        all_reqs.extend(i)


    valid_tickets = []
    for x in lines_nearby_tickets:

        is_valid_ticket = True

        for field_num, x2 in enumerate(x.split(",")):
            x2 = int(x2)

            satisfy_req = [ (r_min <= x2 <= r_max) for r_min, r_max in all_reqs]

            if not  any(satisfy_req):
                is_valid_ticket = False


        if is_valid_ticket:
            valid_tickets.append(x)



    field_possible_values = { i: list(requirements.keys()) for i  in range(len(x.split(","))) }


    for x in valid_tickets:
        for field_num, x2 in enumerate(x.split(",")):
            x2 = int(x2)

            for field_type, field_type_constraints in requirements.items():




                matches_any_constraint_of_fieldtype = [ (r_min <= x2 <= r_max) for r_min, r_max in field_type_constraints]



                if not any(matches_any_constraint_of_fieldtype):
                    if field_type in field_possible_values[field_num]:
                        field_possible_values[field_num].remove(field_type)



    print(field_possible_values)


    
    #for k,v in field_possible_values.items():
    #    print(f" {k} => {len(v)}")
    #    print(f" {k} => {v}")


    #    foo = [x for x in v if x.startswith("departure")]


    #    #print(f" {k} => {foo}")


    still_to_assign = list(requirements.keys())

    field_number = {} 


    finished = False

    remainder = copy.deepcopy(field_possible_values)

    while not finished:

        finished = True


        # Find field numbers with least amount of items

        sorted_list = sorted( [ (k,v) for k,v in remainder.items() ], key=lambda x: len(x[1] ) )


        first_item = sorted_list[0]
        if len(first_item[1]) == 1:
            field_number[first_item[0]] = first_item[1][0]

            del remainder[first_item[0]]

            for v in remainder.values():
                v.remove(first_item[1][0])

            if len(remainder.keys()) == 0:
                finished = True
            else:
                finished = False





    my_ticket_values = [your_ticket_values[k] for k,v in field_number.items() if v.startswith("departure")]

    print(my_ticket_values)

    print(functools.reduce(lambda a,b: a*b, my_ticket_values))

if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_16.txt")
    #part2("foo.txt")
    part2("inputs/day_16.txt")
