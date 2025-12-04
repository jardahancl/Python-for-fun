from collections import namedtuple
import datetime
from dataclasses import dataclass


start = datetime.datetime.now()
problem_nr = __file__.split("/")[-1][0:2]

def parse_input():
    result = []
    for line in open(f'adventofcode/2025/resources/{problem_nr}.txt').read().splitlines():
        result.append(line)
    empty_row = '.' * (len(result[0])+2)
    return [empty_row] + ['.' + r + '.' for r in result] + [empty_row]

def count_neighbors(board, i, j):
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            if board[i + di][j + dj] == '@':
                count += 1

    return count


def get_part1(input):
    board = parse_input()
    count = 0
    for i in range(1, len(board)-1):
        for j in range(1, len(board[0])-1):
            if board[i][j] == '@':
                if count_neighbors(board, i, j) < 4:
                    count += 1
    return count


def print_board(board):
    for row in board:
        print(row)

    
def get_part2(input):
    board = parse_input()
    print_board(board)
    count_all = 0
    count = 1
    while count > 0:
        changing = []
        count = 0
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == '@':
                    if count_neighbors(board, i, j) < 4:
                        changing.append((i, j))
        for (i, j) in changing:
            board[i] = board[i][:j] + '.' + board[i][j+1:]
        count = len(changing)
        count_all += count

    return count_all


part1 = get_part1(input)
part2 = get_part2(input)
print(f'{problem_nr}a - result of part1 is {part1}')
print(f'{problem_nr}b - result of part2 is {part2}')
print(f'Time: {datetime.datetime.now() - start}')
# time part1: 
# time part2: 

