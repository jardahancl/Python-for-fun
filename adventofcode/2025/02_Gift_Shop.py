from collections import namedtuple
import datetime
from dataclasses import dataclass

@dataclass
class Interval:
    start: int
    end: int

start = datetime.datetime.now()
problem_nr = __file__.split("/")[-1][0:2]

def parse_input():
    result = []
    for line in open(f'adventofcode/2025/resources/{problem_nr}.txt').read().splitlines():
        for s in line.split(","):
            if s != '':
                splitted = s.split("-")
                start = int(splitted[0])
                end = int(splitted[1])
                result.append(Interval(start, end))
    return result

def get_invalid_above(n: int, base: int):
    if len(str(n)) % base == 0:
        conditions = int(str(n)[0:len(str(n))//base] * base) < n
        if (conditions):
            return int(str(n)[0:len(str(n))//base]) + 1
        else:
            return int(str(n)[0:len(str(n))//base])
    else:
        return int('1' + '0' * (len(str(n))//base))
    
def get_invalid_below(n: int, base: int):
    if len(str(n)) % base == 0:
        conditions = int(str(n)[0:len(str(n))//base] * base) <= n
        if (conditions):
            return int(str(n)[0:len(str(n))//base])
        else:
            return (int(str(n)[0:len(str(n))//base]) - 1)
    else:
        return int('9' * (len(str(n))//base)) if len(str(n))//base > 0 else 0    

def get_invalid_sum(interval: Interval, periods: list):
    result = []
    for p in periods:
        first_invalid = get_invalid_above(interval.start, p)
        last_invalid = get_invalid_below(interval.end, p)
        # print(interval.start, interval.end)
        # print(range(first_invalid, last_invalid + 1), sum(range(first_invalid, last_invalid + 1)))
        result.extend([int(str(f) * p) for f in range(first_invalid, last_invalid + 1)])
    # print(result)
    return sum(set(result))

def get_part1(input):
    ints = parse_input()
    sum = 0
    for i in ints:
        sum += get_invalid_sum(i, [2])
    return sum    


def get_part2(input):
    ints = parse_input()
    sum = 0
    for i in ints:
        sum += get_invalid_sum(i, [2, 3, 5, 7])
    return sum    


part1 = get_part1(input)
part2 = get_part2(input)
print(f'{problem_nr}a - result of part1 is {part1}')
print(f'{problem_nr}b - result of part2 is {part2}')
print(f'Time: {datetime.datetime.now() - start}')
# time part1: 1:10
# time part2: 3h
