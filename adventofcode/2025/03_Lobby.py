from collections import namedtuple
import datetime
from dataclasses import dataclass


start = datetime.datetime.now()
problem_nr = __file__.split("/")[-1][0:2]

def parse_input():
    result = []
    for line in open(f'adventofcode/2025/resources/{problem_nr}.txt').read().splitlines():
        result.append(line)
    return result

def extract(bank: str, size: int):
    if size == 1:
        return max([int(i) for i in list(bank)])
    else:
        m = max([int(i) for i in list(bank[0:(len(bank)-size+1)])])
        pos = bank.find(str(m))
        return m * (10 ** (size-1)) + extract(bank[pos + 1:], size - 1) 

def get_part1(input):
    banks = parse_input()
    sum = 0
    for bank in banks:
        code = extract(bank, 2)
        sum += code
    return sum

def get_part2(input):
    banks = parse_input()
    sum = 0
    for bank in banks:
        code = extract(bank, 12)
        sum += code
    return sum   


part1 = get_part1(input)
part2 = get_part2(input)
print(f'{problem_nr}a - result of part1 is {part1}')
print(f'{problem_nr}b - result of part2 is {part2}')
print(f'Time: {datetime.datetime.now() - start}')
# time part1: 30m
# time part2: 5m
