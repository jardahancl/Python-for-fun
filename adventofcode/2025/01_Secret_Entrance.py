from collections import namedtuple
import datetime
from dataclasses import dataclass

@dataclass
class Step:
    dir: str
    len: int

start = datetime.datetime.now()
problem_nr = __file__.split("/")[-1][0:2]

def parse_input():
    result = []
    for line in open(f'adventofcode/2025/resources/{problem_nr}.txt').read().splitlines():
        result.append(Step(line[0], int(line[1:])))
    return result


def get_part1(input):
    input = parse_input()
    start = 50
    zeroCount = 0   
    for i in input:
        if i.dir == 'L':
            start +=  int(i.len)
        elif i.dir == 'R':
            start -= int(i.len)
        if start % 100 == 0:
            zeroCount += 1
        
    return zeroCount


def get_part2(input):
    input = parse_input()
    start = 50
    zeroCount = 0   
    for i in input:
        added = 0
        next = 0
        if i.dir == 'L':
            next = (start - int(i.len))
            added -= next // 100
            if start % 100 == 0:
                added -= 1
            if next % 100 == 0:
                added += 1
        elif i.dir == 'R':
            next = (start + int(i.len))
            added += next // 100
        print(f"Start {start}, adding {i.dir}{i.len}, addedcount is {added}, result is {next}")
        zeroCount += added
        start = next % 100

    return zeroCount


part1 = get_part1(input)
part2 = get_part2(input)
print(f'{problem_nr}a - result of part1 is {part1}')
print(f'{problem_nr}b - result of part2 is {part2}')
print(f'Time: {datetime.datetime.now() - start}')
# time part1: 20m
# time part2: 13:12 
# 6145 too high
# 6139 too high
# 6067 too low