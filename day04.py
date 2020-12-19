import os
import itertools


def part1(input_file):
    with open(input_file) as f:
        lines = f.read().split("\n")
    

    new_passport = True

    valid_passports = 0


    required_fields = ["byr" , "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    
    missing_fields = [x for x in required_fields]
    for x in lines:
        if x.strip() == "":

            if len(missing_fields) == 0:
                valid_passports += 1

            if len(missing_fields) == 1  and missing_fields[0] == "cid":
                valid_passports += 1


            missing_fields = [x for x in required_fields]

        else:
            fields = [i.split(":")[0] for i in x.split(" ")]

            for i in fields:
                missing_fields.remove(i)

            


    print(valid_passports)





if __name__ == "__main__":
    part1("inputs/day_04.txt")
    #part2("inputs/day_04.txt")


