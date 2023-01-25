import dataclasses
from collections import namedtuple
from copy import deepcopy


Point = namedtuple('Point', 'row, col')


@dataclasses.dataclass
class Elf:
    position: Point
    pref_directions: list

    def __init__(self, pos: Point, directions: list) -> None:
        self.position = pos
        self.pref_directions = directions

    def is_alone(self, elves: list):
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return self.move_neighbors_possible(elves, neighbours)

    def move_neighbors_possible(self, elves: list, differences):
        for d_row, d_col in differences:
            if Point(self.position.row + d_row, self.position.col + d_col) in elves:
                return False
        return True

    def move_possible(self, direction: str, elves: list):
        if direction == 'N':
            return self.move_neighbors_possible(elves, [(-1, -1), (-1, 0), (-1, 1)])
        elif direction == 'S':
            return self.move_neighbors_possible(elves, [(1, -1), (1, 0), (1, 1)])
        elif direction == 'W':
            return self.move_neighbors_possible(elves, [(-1, -1), (0, -1), (1, -1)])
        elif direction == 'E':
            return self.move_neighbors_possible(elves, [(-1, 1), (0, 1), (1, 1)])

    def move_in_direction(self, direction):
        if direction == 'N':
            return Point(self.position.row - 1, self.position.col)
        elif direction == 'S':
            return Point(self.position.row + 1, self.position.col)
        elif direction == 'W':
            return Point(self.position.row, self.position.col - 1)
        elif direction == 'E':
            return Point(self.position.row, self.position.col + 1)

    def next_position(self, elves: list):
        future_self = deepcopy(self)
        if self.is_alone(elves):
            return future_self.position
        for i in range(4):
            direction = future_self.pref_directions[i]
            if future_self.move_possible(direction, elves):
                return future_self.move_in_direction(direction)
        return future_self.position

    def update_direction(self):
        future_pref_directions = deepcopy(self.pref_directions)
        applied_direction = future_pref_directions.pop(0)
        future_pref_directions.append(applied_direction)
        return future_pref_directions


def elves_shape(elves):
    row_min = min([x.position.row for x in elves.values()])
    row_max = max([x.position.row for x in elves.values()])
    col_min = min([x.position.col for x in elves.values()])
    col_max = max([x.position.col for x in elves.values()])
    return [[row_min, row_max], [col_min, col_max]]


# def display(elves):
#     shape = elves_shape(elves)
#     result = 0
#     for row in range(shape[0][0], shape[0][1] + 1):
#         for col in range(shape[1][0], shape[1][1] + 1):
#             if Point(row, col) in elves:
#                 print('#', end='')
#             else:
#                 result += 1
#                 print('.', end='')
#         print('')
#     print('')
#     return result


def move_elves(elves):
    future_elves = {}
    for _, elf in elves.items():
        future_position = elf.next_position(elves)
        if future_position in future_elves:
            future_elves[elf.position] = elf
            future_elves[future_elves[future_position].position] = future_elves[future_position]
            future_elves.pop(future_position)
        else:
            future_elves[future_position] = elf
    for key, elf in future_elves.items():
        elf.position = key
        elf.pref_directions = elf.update_direction()
    return future_elves


elves_base = {}
with open('resources/23.txt') as file:
    lines = file.read().splitlines()

for row, line in enumerate(lines):
    for col, s in enumerate(line):
        if s == '#':
            position = Point(row, col)
            elves_base[position] = Elf(position, ['N', 'S', 'W', 'E'])


elves_1 = deepcopy(elves_base)
for i in range(10):
    next_elves = move_elves(elves_1)
    elves_1 = next_elves
shape = elves_shape(elves_1)
sol_1 = (shape[0][1] - shape[0][0] + 1) * (shape[1][1] - shape[1][0] + 1) - len(elves_1.keys())
print(f'23a - There are {sol_1} empty places after 10 rounds')


elves_2 = deepcopy(elves_base)
step = 0
while True:
    next_elves = move_elves(elves_2)
    step += 1
    if next_elves == elves_2:
        break
    elves_2 = next_elves
print(f'23b - Situation gets immobile after {step} rounds')
# time 5h











