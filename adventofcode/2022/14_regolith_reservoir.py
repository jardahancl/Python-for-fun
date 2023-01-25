def traverse_w(st, en):
    result = []
    if st[0] != en[0]:
        minimal = min(st[0], en[0])
        for i in range(minimal, max(st[0], en[0]) + 1):
            result.append([i, st[1]])
    if st[1] != en[1]:
        minimal = min(st[1], en[1])
        for i in range(minimal, max(st[1], en[1]) + 1):
            result.append([st[0], i])
    return result


def visualize():
    for y in range(start[1], range_walls[1][1] + 4):
        for x in range(range_walls[0][0] - 1, range_walls[0][1] + 2):
            if (x, y) in board:
                print(board[(x, y)], end='')
            else:
                print('.', end='')
        print('')
    print('')


def add_sand():
    seed = start.copy()
    while range_walls[1][1] >= seed[1]:
        for step in [(0, 1), (-1, 1), (1, 1)]:
            next = [seed[0] + step[0], seed[1] + step[1]]
            if tuple(next) not in board:
                seed = next
                break
        if seed != next:
            if seed == start:
                return False
            else:
                board[tuple(seed)] = 'o'
            return True
    return False


with open('resources/14.txt') as f:
    lines = f.read().splitlines()

walls = []
for line in lines:
    wall = list(map(lambda x: [int(x.split(',')[0]), int(x.split(',')[1])], line.split(' -> ')))
    walls.append(wall)
# pprint(walls)

start = [500, 0]
c_vert = [c[0] for wall in walls for c in wall]
c_hor = [c[1] for wall in walls for c in wall]
range_walls = [[min(c_vert), max(c_vert)], [min(c_hor), max(c_hor)]]
# print(range_walls, start)

board = {}
for wall in walls:
    for w1, w2 in zip(wall, wall[1:]):
        for b in traverse_w(w1, w2):
            if tuple(b) not in board:
                board[tuple(b)] = '#'

count = 0
while add_sand():
    count += 1
# visualize()
print(f'14a - falling into abyss starts after {count} units of sand')

range_walls[0][0] = range_walls[0][0] - range_walls[1][1] - 1
range_walls[0][1] = range_walls[0][1] + range_walls[1][1] + 1
range_walls[1][1] += 2
for i in range(range_walls[0][0], range_walls[0][1]):
    board[(i, range_walls[1][1])] = '#'
# visualize()
while add_sand():
    count += 1
# visualize()
print(f'14b - pile is full after {count + 1} units of sand')
# time 2h 30m








