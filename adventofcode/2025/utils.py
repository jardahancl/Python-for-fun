from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Interval:
    start: int
    end: int
    

def parse_board(problem_nr: str, wall_char: str):
    result = []
    for line in open(f'adventofcode/2025/resources/{problem_nr}.txt').read().splitlines():
        result.append(line)
    empty_row = wall_char * (len(result[0])+2)
    return [empty_row] + [wall_char + r + wall_char for r in result] + [empty_row]


def print_board(board):
    for row in board:
        print(row)


