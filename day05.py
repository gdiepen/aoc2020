
import os
import itertools



def part1(input_file):
    with open(input_file) as f:
        lines = f.read().split("\n")
    lines = [x for x in lines if x != ""]


    _max = 0 

    for x in lines:
        foo = x.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")


        _row = int(foo[0:7], 2)
        _col = int(foo[7:], 2)


        seat_id = _row * 8 + _col


        _max = max(seat_id, _max)


    print(_max)


def part2(input_file):
    with open(input_file) as f:
        lines = f.read().split("\n")
    lines = [x for x in lines if x != ""]


    _max = 0 

    _list = []

    for x in lines:
        foo = x.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")


        _row = int(foo[0:7], 2)
        _col = int(foo[7:], 2)


        seat_id = _row * 8 + _col

        _list.append(seat_id)

    _list = sorted(_list)

    _list2 = range(_list[0], _list[-1]+1)

    print([x for x in _list2 if x not in _list])

if __name__ == "__main__":
    part1("inputs/day_05.txt")
    part2("inputs/day_05.txt")

