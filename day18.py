import os
import copy
import itertools
import re
import collections
import math
import functools


class I(int):
    def __add__(a, b): return I(a.real + b.real)
    def __sub__(a, b): return I(a.real * b.real)
    __mul__ = __add__

def part1(input_file):
    with open(input_file) as f:
        lines = f.read().strip()

    total_sum = 0 

    for x in lines.split("\n"):

        finished = False

        while not finished:
            finished = True


            foo = re.findall(r"\(\d+\)", x)
            if foo:
                new_value = foo[0].replace("(", "").replace(")","")

                x = x.replace(foo[0], new_value, 1)

                finished = False
            else:

                foo = re.findall(r"(\d+) (\*|\+) (\d+)", x)
                if foo:
                    _val1 = int(foo[0][0])
                    _val2 = int(foo[0][2])

                    _operator = foo[0][1]

                    if _operator == "+":
                        new_value = str( _val1 + _val2)
                    else:
                        new_value = str( _val1 * _val2)

                    x = x.replace(" ".join(foo[0]), new_value, 1)

                    finished = False

            
        total_sum += int(x)
        print(x)

    print(total_sum)


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().strip()

    total_sum = 0 
    
    for x in lines.split("\n"):


        foobar = re.sub(r"(\d+)", r"I(\1)", x).replace("*", "-")
        print(foobar)
        _answer = eval(foobar.replace("+", "*"))




        finished = False

        print(x)

        while not finished:
            finished = True


            print()
            print(f"    {x}")

            foo = re.findall(r"\(\d+\)", x)
            if foo:

                print(f"        (A)")
                print(f"        {foo[0]}")
                new_value = foo[0].replace("(", "").replace(")","")

                x = x.replace(foo[0], new_value, 1)

                finished = False
            else:
                # First do anything within parenthesis
                foo = re.findall(r"\((\d+) (\*) (\d+)\)", x)
                if foo:
                    print(f"        (A * B)")
                    print(f"        {foo[0]}")
                    _val1 = int(foo[0][0])
                    _val2 = int(foo[0][2])

                    _operator = foo[0][1]

                    if _operator == "+":
                        new_value =  str( _val1 + _val2)
                    else:
                        new_value = str( _val1 * _val2)

                    x = x.replace(" ".join(foo[0]), new_value, 1)

                    finished = False
                
                else:

                    foo = re.findall(r"(\d+) (\+) (\d+)", x)
                    if foo:
                        print(f"        A + B")
                        print(f"        {foo[0]}")


                        _val1 = int(foo[0][0])
                        _val2 = int(foo[0][2])

                        _operator = foo[0][1]

                        if _operator == "+":
                            new_value = str( _val1 + _val2)
                        else:
                            new_value = str( _val1 * _val2)

                        x = x.replace(" ".join(foo[0]), new_value, 1)

                        finished = False

                    else:


                        # First do anything within parenthesis
                        foo = re.findall(r"\((\d+) (\*) (\d+)", x)
                        if foo:
                            print(f"        (A * B)")
                            print(f"        {foo[0]}")
                            _val1 = int(foo[-1][0])
                            _val2 = int(foo[-1][2])

                            _operator = foo[-1][1]

                            if _operator == "+":
                                new_value =  str( _val1 + _val2)
                            else:
                                new_value = str( _val1 * _val2)

                            x = x.replace(" ".join(foo[-1]), new_value, 1)

                            finished = False

                        else: 


                            foo = re.findall(r"(\d+) (\*) (\d+)", x)
                            if foo:
                                print(f"        A * B")
                                print(f"        {foo[0]}")
                                _val1 = int(foo[0][0])
                                _val2 = int(foo[0][2])

                                _operator = foo[0][1]

                                if _operator == "+":
                                    new_value = str( _val1 + _val2)
                                else:
                                    new_value = str( _val1 * _val2)

                                x = x.replace(" ".join(foo[0]), new_value, 1)

                                finished = False
        if str(x) != str(_answer):
            print("ERROR")
            print(f"We got {x} and answer is {_answer}")
           

        total_sum += int(x)
        print(x)

    print(total_sum)



def part2_B(input_file):
    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    import re
    import sys
        

    lines2 = []
    for line in lines:
        lines2.append( re.sub(r"(\d+)", r"I(\1)", line).replace("*", "-"))
        

    #print(sum(eval(line) for line in lines2))
    print(sum(eval(line.replace("+", "*")) for line in lines2))





if __name__ == "__main__":
    #part1("foo.txt")
    #part1("inputs/day_18.txt")
    #part2("foo.txt")
    part2("inputs/day_18.txt")
    #part2_B("inputs/day_18.txt")

