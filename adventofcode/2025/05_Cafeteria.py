import datetime
import utils
from dataclasses import dataclass
import itertools



@dataclass
class Interval:
    start: int
    end: int


start = datetime.datetime.now()
problem_nr = __file__.split("/")[-1][0:2]

def parse_input():
    ranges = []
    available = []
    for line in open(f'adventofcode/2025/resources/{problem_nr}.txt').read().splitlines():
        if '-' in line:
            splits = line.split('-')
            ranges.append(Interval(int(splits[0]), int(splits[1])))
        elif len(line) > 0:
            available.append(int(line))

    return ranges, available


def get_part1(input):
    ints, available = parse_input()
    count = 0
    for a in available:
        if any([a >= interval.start and a <= interval.end for interval in ints]):
            count += 1
    return count

    r
def get_part2(input):
    ints, available = parse_input()
    count = 0
    breaks = sorted(list(set(itertools.chain.from_iterable(list([[i.start, i.end] for i in ints])))))
    for i, j in zip(breaks, breaks[1:]):
        if j - i <= 1:
            count += 1
        elif j - i > 1:
            a = i+1
            if any([a >= interval.start and a <= interval.end for interval in ints]):
                count += (j - i)
            else:
                count += 1
    return count + 1
        
part1 = get_part1(input)
part2 = get_part2(input)
print(f'{problem_nr}a - result of part1 is {part1}')
print(f'{problem_nr}b - result of part2 is {part2}')
print(f'Time: {datetime.datetime.now() - start}')
# time part1: 10m
# time part2: 40m
