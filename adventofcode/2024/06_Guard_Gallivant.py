from dataclasses import dataclass


@dataclass
class Point:
    row: int
    col: int


def extend(board, n, wall):
    board_in = board.copy()
    for i in range(n):
       for l in range(len(board_in)):
           board_in[l] = wall + board_in[l] + wall
       board_in = [wall * len(board_in[0])] + board_in + [wall * len(board_in[0])]
    return board_in


def find_start(board):
    for l in range(len(board)):
        for c in range(len(board[0])):
            if board[l][c] == '^':
                return Point(l, c)


def get_next(pos, dir):
    if dir == '^':
        return Point(pos.row - 1, pos.col)
    if dir == 'v':
        return Point(pos.row + 1, pos.col)
    if dir == '<':
        return Point(pos.row, pos.col - 1)
    if dir == '>':
        return Point(pos.row, pos.col + 1)


def turn(dir):
    if dir == '^':
        return '>'
    if dir == 'v':
        return '<'
    if dir == '<':
        return '^'
    if dir == '>':
        return 'v'


def board_update(board, row, col):
    result = []
    for l in range(len(board)):
        line = ''
        for c in range(len(board[0])):
            added = '#' if (l == row and c == col) else board[l][c]
            line = line + added
        result.append(line)
    return result


def get_visited(board):
    visited = {}

    start = find_start(board)
    visited[(start.row, start.col)] = set('^')

    pos = start
    dir = board[start.row][start.col]

    loop = False
    while True:
        try:
            next = get_next(pos, dir)
            if next.row == -1 or next.col == -1:
                break
            next_dir = dir
            if board[next.row][next.col] == '#':
                next_dir = turn(next_dir)
                next = get_next(pos, next_dir)
            if board[next.row][next.col] == '#':
                next_dir = turn(next_dir)
                next = get_next(pos, next_dir)
            if board[next.row][next.col] == '#':
                next_dir = turn(next_dir)
                next = get_next(pos, next_dir)
            if visited.keys().__contains__((next.row, next.col)) and visited[(next.row, next.col)].__contains__(
                        next_dir):
                loop = True
                break
            if visited.keys().__contains__((next.row, next.col)):
                visited[(next.row, next.col)].add(next_dir)
            else:
                visited[(next.row, next.col)] = set(next_dir)
            pos = next
            dir = next_dir
        except IndexError:
            loop = False
            break
    return visited, loop


board = []
for line in open('resources/06.txt').read().splitlines():
    board.append(line)

visited_set, is_loop = get_visited(board)

start_point = find_start(board)
loopfull_walls = set()
for r, c in visited_set.keys():
    if r != start_point.row or c != start_point.col:
        board_plus = board_update(board, r, c)
        visited_plus, is_loop = get_visited(board_plus)
        if is_loop:
            loopfull_walls.add((r, c))


print(f'06a - visited positions count is {len(visited_set)}')
print(f'06b - loopfull wall count is {len(loopfull_walls)}')
# 40m + 2h 20m = 3h

