import itertools
from dataclasses import dataclass


@dataclass
class Frequency:
    alias: str
    positions: list[(int, int)]


def get_antinodes_v2(positions, length, height):
    res = set()
    for p1, p2 in itertools.combinations(positions, 2):
        k = 1
        while True:
            if check_inside(p1[0] + k * (p1[0] - p2[0]), p1[1] + k * (p1[1] - p2[1]), length, height):
                res.add((p1[0] + k * (p1[0] - p2[0]), p1[1] + k * (p1[1] - p2[1])))
                k += 1
            else:
                break
        k = 0
        while True:
            if check_inside(p1[0] + k * (p1[0] - p2[0]), p1[1] + k * (p1[1] - p2[1]), length, height):
                res.add((p1[0] + k * (p1[0] - p2[0]), p1[1] + k * (p1[1] - p2[1])))
                k += -1
            else:
                break
    return res


def check_inside(x, y, length, height):
    return (x >= 0) and (y >= 0) and (x < length) and (y < height)


def get_antinodes_v1(positions, length, height):
    res = set()
    for p1, p2 in itertools.combinations(positions, 2):
        if check_inside(2 * p1[0] - p2[0], 2 * p1[1] - p2[1], length, height):
            res.add((2 * p1[0] - p2[0], 2 * p1[1] - p2[1]))
        if check_inside(2 * p2[0] - p1[0], 2 * p2[1] - p1[1], length, height):
            res.add((2 * p2[0] - p1[0], 2 * p2[1] - p1[1]))
    return res


board = []
for line in open('resources/08.txt').read().splitlines():
    board.append(line)

frequencies = {}
for l in range(len(board)):
    for c in range(len(board[l])):
        f = board[l][c]
        if f != '.':
            if frequencies.keys().__contains__(f):
                frequencies[f].append((l, c))
            else:
                frequencies[f] = [(l, c)]


antinodes_v1 = {}
for f in frequencies.keys():
    antinodes_v1[f] = get_antinodes_v1(frequencies[f], len(board), len(board[0]))
antinodes_v2 = {}
for f in frequencies.keys():
    antinodes_v2[f] = get_antinodes_v2(frequencies[f], len(board), len(board[0]))


res1 = set()
for k in antinodes_v1.keys():
    print(antinodes_v1[k])
    res1 = res1.union(antinodes_v1[k])
res2 = set()
for k in antinodes_v2.keys():
    print(antinodes_v2[k])
    res2 = res2.union(antinodes_v2[k])


print(f'08a - antinode count is {len(res1)}')
print(f'08b - enhanced antinode count is {len(res2)}')
# 1h + 10m = 1h 10m