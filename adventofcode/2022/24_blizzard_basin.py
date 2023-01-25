from collections import namedtuple
from pprint import pprint


Point = namedtuple('Point', 'row, col')
State = namedtuple('State', 'row, col, step')


def add_winds(winds, key, value):
    if key in winds:
        winds[key].append(value)
    else:
        winds[key] = [value]


def in_bounds(state):
    if state.row < 0 or state.row > height - 1:
        return False
    if state.col < 0 or state.col > length - 1:
        return False
    return True


def no_blizzards(state):
    if state.row in right_winds and (state.col - state.step) % length in right_winds[state.row]:
        return False
    if state.row in left_winds and (state.col + state.step) % length in left_winds[state.row]:
        return False
    if state.col in down_winds and (state.row - state.step) % height in down_winds[state.col]:
        return False
    if state.col in up_winds and (state.row + state.step) % height in up_winds[state.col]:
        return False
    return True


def walk(actual_step: int, starting_point: Point, ending_point: Point):
    min_step = actual_step
    q = [State(starting_point.row, starting_point.col, actual_step)]
    while True:
        state = q.pop(0)
        if state.step >= min_step:
            min_step += 1
            if no_blizzards(State(starting_point.row, starting_point.col, min_step)):
                q.append(State(starting_point.row, starting_point.col, min_step))
        if state.row == ending_point.row and state.col == ending_point.col:
            break
        else:
            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
                new_state = State(state.row + dr, state.col + dc, state.step + 1)
                if in_bounds(new_state):
                    if no_blizzards(new_state):
                        if new_state not in q:
                            q.append(new_state)
    return state


with open('resources/24.txt') as file:
    lines = file.read().splitlines()

# initialize (winds)
height = len(lines) - 2
length = len(lines[0]) - 2
right_winds, left_winds, up_winds, down_winds = {}, {}, {}, {}
for i, row in enumerate(lines[1:-1]):
    for j, s in enumerate(row[1:-1]):
        if s == '>':
            add_winds(right_winds, i, j)
        if s == '<':
            add_winds(left_winds, i, j)
        if s == 'v':
            add_winds(down_winds, j, i)
        if s == '^':
            add_winds(up_winds, j, i)
start = Point(0, 0)
end = Point(height - 1, lines[-1].find('.') - 1)

# part 1 - way to the end
state = walk(1, start, end)
print(f'24a - Final result is {state.step + 1}.')

# part 2 - way back
state = State(end.row, end.col, state.step + 2)
while not no_blizzards(state):
    state = State(state.row, state.col, state.step + 1)
state = walk(state.step, end, start)
# part 2 - way to the end again
state = State(start.row, start.col, state.step + 2)
while not no_blizzards(state):
    state = State(state.row, state.col, state.step + 1)
state = walk(state.step, start, end)
print(f'24b - Final result is {state.step + 1}.')
# time 6h


# @dataclasses.dataclass
# class Board:
#     name: str
#     start: Point
#     end: Point
#     you: Point
#     height: int
#     length: int
#     winds: dict
#
#     def __init__(self, name: str, info: list) -> None:
#         self.name = name
#         self.height = len(info)
#         self.length = len(info[0])
#         self.start = Point(0, info[0].find('.'))
#         self.end = Point(self.height - 1, info[self.height - 1].find('.'))
#         self.you = deepcopy(self.start)
#         self.boarders = []
#         for col in range(self.length):
#             if col == self.start.col:
#                 self.boarders.append((-1, col))
#             else:
#                 self.boarders.append((0, col))
#             if col == self.end.col:
#                 self.boarders.append((self.height, col))
#             else:
#                 self.boarders.append((self.height - 1, col))
#         for row in range(1, self.height - 1):
#             self.boarders.append((row, 0))
#             self.boarders.append((row, self.length-1))
#         self.winds = {}
#         for row, line in enumerate(info):
#             for col, s in enumerate(line):
#                 if s in ['<', '>', 'v', '^']:
#                     self.winds[(row, col)] = ([Wind(row, col, s)])
#
#     def display(self):
#         print()
#         for row in range(self.height):
#             for col in range(self.length):
#                 pos = (row, col)
#                 if pos in [(self.start.row, self.start.col), (self.end.row, self.end.col)]:
#                     print('.', end='')
#                 elif pos in self.boarders:
#                     print('#', end='')
#                 elif pos == (self.you.row, self.you.col):
#                     print('E', end='')
#                 elif pos in self.winds:
#                     if len(self.winds[pos]) == 1:
#                         print(self.winds[pos][0].dir, end='')
#                     else:
#                         print(len(self.winds[pos]), end='')
#                 else:
#                     print('.', end='')
#             print('')
#
#     def step_winds(self):
#         new_winds = {}
#         for key, w in self.winds.items():
#             for wind in w:
#                 new_wind = self.step_wind(wind)
#                 new_key = (new_wind.row, new_wind.col)
#                 if new_key in new_winds:
#                     new_winds[new_key].append(new_wind)
#                 else:
#                     new_winds[new_key] = [new_wind]
#         self.winds = new_winds
#
#     def step_wind(self, wind):
#         if wind.dir == '>':
#             return Wind(wind.row, (wind.col % (self.length - 2)) + 1, wind.dir)
#         elif wind.dir == '<':
#             return Wind(wind.row, ((wind.col - 2) % (self.length - 2)) + 1, wind.dir)
#         elif wind.dir == '^':
#             return Wind(((wind.row - 2) % (self.height - 2)) + 1, wind.col, wind.dir)
#         elif wind.dir == 'v':
#             return Wind((wind.row % (self.height - 2)) + 1, wind.col, wind.dir)


# boards = [start_board]
# for _ in range((start_board.length - 2) * (start_board.height - 2)):
#     last_board = deepcopy(boards[-1])
#     last_board.step_winds()
#     boards.append(last_board)
# positions = [(start_board.you, 0)]
# current_step = 0
# while True:
#     position = positions.pop(0)
#     you = position[0]
#     step = position[1]
#     if step > 5:
#         break
#     if step > current_step:
#         current_step += 1
#         print(step, position)
#     if you == start_board.end:
#         print(f'Final result {position}')
#         break
#     else:
#         for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
#             new_board = deepcopy(boards[step + 1])
#             new_you = Point(you.row + dr, you.col + dc)
#             if new_you not in new_board.boarders:
#                 if new_you not in new_board.winds:
#                     if (new_you, step + 1) not in positions:
#                         positions.append((new_you, step + 1))






