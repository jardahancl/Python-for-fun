from queue import Queue
from collections import namedtuple
from adventofcode import common as cm

board = []
for line in open('resources/12.txt').read().splitlines():
    board.append(line)
Garden = namedtuple('Garden', ['symbol', 'positions', 'area', 'perimeter', 'side_count'])
plot = cm.extend(board, 1, '.')


def get_side_count(side_pairs):
    side_count = 0
    for s in side_pairs:
        # on same line
        if s[0][0] == s[1][0]:
            pos = s[0]
            pos_up = (pos[0] - 1, pos[1])
            neigh = s[1]
            neigh_up = (neigh[0] - 1, neigh[1])
            if (pos_up, neigh_up) not in side_pairs:
                side_count += 1
        # on same column
        elif s[0][1] == s[1][1]:
            pos = s[0]
            pos_left = (pos[0], pos[1] - 1)
            neigh = s[1]
            neigh_left = (neigh[0], neigh[1] - 1)
            if (pos_left, neigh_left) not in side_pairs:
                side_count += 1
    return side_count


def extract_garden(start, plot):
    symbol = plot[start[0]][start[1]]
    positions = set()
    positions.add((start[0], start[1]))
    q = Queue()
    q.put(start)
    while not q.empty():
        curr = q.get()
        for d in cm.dirs4:
            next = (curr[0] + d[0], curr[1] + d[1])
            if plot[next[0]][next[1]] == symbol and next not in positions:
                q.put(next)
                positions.add(next)

    perimeter = 0
    side_pairs = [] # positions where neighbour is not in positions
    for pos in positions:
        for d in cm.dirs4:
            neigh = (pos[0] + d[0], pos[1] + d[1])
            if plot[neigh[0]][neigh[1]] != symbol:
                perimeter += 1
                side_pairs.append((pos, neigh))
    side_count = get_side_count(side_pairs)
    area = len(positions)
    return Garden(symbol, positions, area, len(side_pairs), side_count)


gardens = [] # [symbol, positions, area, perimeter, side_count]
visited = []
for l in range(len(plot)):
    for c in range(len(plot[l])):
        if plot[l][c] != '.' and (l, c) not in visited:
            garden = extract_garden((l, c), plot)
            visited = visited + list(garden.positions)
            gardens.append(garden)


fencing_price = sum([g.perimeter * g.area for g in gardens])
fencing_price_v2 = sum([g.side_count * g.area for g in gardens])

print(f'12a - price for fencing is {fencing_price}')
print(f'12b - price for fencing is {fencing_price_v2}')
# 1h + 40m
