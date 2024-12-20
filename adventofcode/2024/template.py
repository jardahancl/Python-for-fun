from collections import namedtuple
import datetime


start = datetime.datetime.now()
problem_nr = __file__.split("\\")[-1][0:2]
robots = []
for line in open(f'resources/{problem_nr}t.txt').read().splitlines():

    input.append(line)


def get_part1(input):
    pass


def get_part2(input):
    pass


part1 = get_part1(input)
# part2 = get_part2(input)
# print(f'{problem_nr}a - result of part1 is {part1}')
# print(f'{problem_nr}b - result of part2 is {part2}')
print(f'Time: {datetime.datetime.now() - start}')
# time part1:
# time part2:


