import os
import itertools
import re


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


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().split("\n")
    

    valid_passports = 0


    required_fields = ["byr" , "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    current_passport = {}

    for x in lines:
        if x.strip() == "":
            is_valid = True

            print(current_passport)

            if int(current_passport.get("byr", 0)) < 1920  or (int(current_passport.get("byr",0))>2002):
                is_valid = False

            print(f"    isvalid = {is_valid}")
            

            if int(current_passport.get("iyr", 0)) < 2010  or (int(current_passport.get("iyr",0))>2020):
                is_valid = False
            print(f"    isvalid = {is_valid}")

            if int(current_passport.get("eyr", 0)) < 2020  or (int(current_passport.get("eyr",0))>2030):
                is_valid = False
            print(f"    isvalid = {is_valid}")

            _height = current_passport.get("hgt","")
            foo = re.match(r"(\d{2,3})(cm|in)", _height)

            if foo is not None:

                _length = int(foo.groups()[0])
                if foo.groups()[1] == "cm":
                    if (_length < 150) or (_length > 193):
                        is_valid = False
                if foo.groups()[1] == "in":
                    if (_length < 59) or (_length > 76):
                        is_valid = False

            else:
                is_valid=False

            print(f"    isvalid = {is_valid}")
            
            if not re.match(r"#[0-9a-f]{6}", current_passport.get("hcl","")):
                is_valid = False
            print(f"    isvalid = {is_valid}")

            if current_passport.get("ecl", "") not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                is_valid = False
            print(f"    isvalid = {is_valid}")


            if not re.match(r"^\d{9}$", current_passport.get("pid","")):
                is_valid = False
            print(f"    isvalid = {is_valid}")


            if is_valid:
                valid_passports += 1

            print(current_passport)

            current_passport = {}
        else:
            current_passport.update( { i.split(":")[0]: i.split(":")[1] for i in  x.split(" ")} )

    print(valid_passports)



if __name__ == "__main__":
    part1("inputs/day_04.txt")
    part2("inputs/day_04.txt")


