from collections import namedtuple
import re
import datetime

from numpy.ma.core import max_val

dirs4 = [[1, 0], [-1, 0], [0, 1], [0, -1]]

start = datetime.datetime.now()
problem_nr = __file__.split("\\")[-1][0:2]
Robot = namedtuple('Robot', ['px', 'py', 'vx', 'vy'])
robots = []
for line in open(f'resources/{problem_nr}.txt').read().splitlines():
    numbers = list(map(lambda x: int(x), re.findall(r'-?\b\d+\b', line)))
    robot = Robot(numbers[0], numbers[1], numbers[2], numbers[3])
    robots.append(robot)

board_size_test = [11, 7] # width, height
board_size_prod = [101, 103]
seconds = 100

def get_positions(size, secs):
    positions = []
    for robot in robots:
        rx = (robot.px + secs * robot.vx) % size[0]
        ry = (robot.py + secs * robot.vy) % size[1]
        positions.append([rx, ry])
    return positions


def get_part1(size, secs):
    positions = get_positions(size, secs)
    q1 = [1 if p[0] < (size[0]-1) / 2 and p[1] < (size[1]-1) / 2 else 0 for p in positions]
    q2 = [1 if p[0] > (size[0]-1) / 2 and p[1] < (size[1]-1) / 2 else 0 for p in positions]
    q3 = [1 if p[0] < (size[0]-1) / 2 and p[1] > (size[1]-1) / 2 else 0 for p in positions]
    q4 = [1 if p[0] > (size[0]-1) / 2 and p[1] > (size[1]-1) / 2 else 0 for p in positions]
    return sum(q1) * sum(q2) * sum(q3) * sum(q4)

def get_part2(size):
    res = []
    for s in range(10_000):
        positions = get_positions(size, s)
        nc = 0
        for p in positions:
            for d in dirs4:
                if positions.__contains__([p[0] + d[0], p[1] + d[1]]):
                    nc += 1

        if nc > 300:
            print(f'{s} seconds: ')
            for y in range(size[1]):
                line = ''
                for x in range(size[0]):
                    line += '#' if [x, y] in positions else '.'
                print(line)
            print()
            res.append([s, nc])
    max_val = max([r[1] for r in res])
    max_secs = [r[0] if r[1] == max_val else 0 for r in res]
    return max(max_secs)


part1 = get_part1(board_size_prod, seconds)
part2 = get_part2(board_size_prod)
print(f'{problem_nr}a - result of part1 is {part1}')
print(f'{problem_nr}b - result of part2 is {part2}')
print(f'Time: {datetime.datetime.now() - start}')
# 30m + 45m


