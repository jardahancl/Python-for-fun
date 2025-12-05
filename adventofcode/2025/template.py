import datetime
from dataclasses import dataclass

@dataclass
class Block:
    len: int
    id: int

start = datetime.datetime.now()
problem_nr = __file__.split("\\")[-1][0:2]

def parse_input():
    result = []
    for line in open(f'adventofcode/2025/resources/{problem_nr}t.txt').read().splitlines():
        pass
    return result


def get_part1(input):
    input = parse_input()
    pass


def get_part2(input):
    input = parse_input()
    pass


part1 = get_part1(input)
# part2 = get_part2(input)
# print(f'{problem_nr}a - result of part1 is {part1}')
# print(f'{problem_nr}b - result of part2 is {part2}')
print(f'Time: {datetime.datetime.now() - start}')
# time part1:
# time part2:


