import dataclasses
from copy import copy


@dataclasses.dataclass
class Rock:
    name: int
    height: int
    length: int
    shape: list()

    def __init__(self, name: str, shape: list) -> None:
        self.name = name
        self.length = len(shape[0])
        self.height = len(shape)
        self.shape = shape


@dataclasses.dataclass
class Rocks:
    rock_supply: list
    next_index: int

    def __init__(self) -> None:
        rock_H = Rock('Minus', ['@@@@'])
        rock_X = Rock('Plus', ['.@.', '@@@', '.@.'])
        rock_L = Rock('Ell', ['..@', '..@', '@@@'])
        rock_I = Rock('Iii', ['@', '@', '@', '@'])
        rock_O = Rock('Square', ['@@', '@@'])
        self.rock_supply = [rock_H, rock_X, rock_L, rock_I, rock_O]
        self.next_index = 0

    def next(self):
        rock = self.rock_supply[self.next_index]
        self.next_index = (self.next_index + 1) % len(self.rock_supply)
        return rock

    def reset(self):
        self.next_index = 0


@dataclasses.dataclass
class Field:
    layers: list
    height: int  # total height of the field
    heights: list  # heights of columns visible from top
    heights_subtracted: int  # height not visible from the top
    rock: Rock
    rock_position: list
    move_count: int
    round: int

    def __init__(self) -> None:
        self.layers = ['+-------+']
        self.height = 0
        self.heights = ['puff', 0, 0, 0, 0, 0, 0, 0, 'puff']
        self.heights_subtracted = 0
        self.rock = None
        self.rock_position = None
        self.move_count = 0
        self.round = 0

    def display(self, limit: int):
        print(self.heights)
        to_print = []
        # prepare board to print
        for i in range(limit + 1):
            to_print.append(self.layers[self.height - i])
        # add lines if rock is above height
        if self.rock is not None:
            for _ in range(self.rock_position[0] - self.height):
                to_print.append('|.......|')
        # printing
        for ln in to_print:
            print(ln)
        print()

    def add_line(self, layer: str):
        self.layers.append(layer)
        self.height += 1

    def add_empty_line(self):
        self.layers.append('|.......|')
        self.height += 1

    def has_rock(self):
        return self.rock is not None

    def add_rock(self, rock: Rock):
        for _ in range(3):
            self.add_empty_line()
        for i in range(rock.height):
            layer = '|..' + rock.shape[rock.height - 1 - i] + ('.' * (5 - rock.length)) + '|'
            self.add_line(layer)
        self.rock = rock
        self.rock_position = [self.height, 3]
        self.round += 1
        # print(f'In round {self.round}: Adding rock - {rock.name}')
        # self.display()

    def update_heights(self):
        min_height = min(x for x in self.heights[1:8])
        if min_height > 0:
            self.heights = ['puff'] + [x - min_height for x in self.heights[1:8]] + ['puff']
            self.heights_subtracted += min_height

    def move_possible(self, direction: str):
        if direction == '>':
            for i in range(self.rock.height):
                if '@#' in self.layers[self.rock_position[0] - i] or '@|' in self.layers[self.rock_position[0] - i]:
                    return False
        elif direction == '<':
            for i in range(self.rock.height):
                if '#@' in self.layers[self.rock_position[0] - i] or '|@' in self.layers[self.rock_position[0] - i]:
                    return False
        return True

    def move(self, direction: str):
        if self.has_rock() is None:
            print(f'Move {direction} not possible - there is no active block')
            pass
        if self.move_possible(direction):
            if direction == '>':
                for i in range(self.rock.height):
                    current_line = self.layers[self.rock_position[0] - i]
                    new_line = '|'
                    for b, a in zip(current_line[:-1], current_line[1:]):
                        if b == '@' and a != '|':
                            new_line += b
                        elif a == '@':
                            new_line += '.'
                        else:
                            new_line += a
                    self.layers[self.rock_position[0] - i] = new_line
                self.rock_position[1] += 1
            elif direction == '<':
                for i in range(self.rock.height):
                    current_line = self.layers[self.rock_position[0] - i]
                    new_line = ''
                    for a, b in zip(current_line[:-1], current_line[1:]):
                        if b == '@' and a != '|':
                            new_line += b
                        elif a == '@':
                            new_line += '.'
                        else:
                            new_line += a
                    new_line += '|'
                    self.layers[self.rock_position[0] - i] = new_line
                self.rock_position[1] -= 1
            # print(f'Moving {direction}')
            # self.display()
        else:
            pass
            # print(f'Move {direction} not possible - something in the way')

        self.move_count += 1

    def fall_possible(self):
        for i in range(self.rock.length):
            v = 0
            while self.rock.shape[-1 - v][i] != '@':
                v += 1
            below_rock = self.layers[self.rock_position[0] - self.rock.height + v][self.rock_position[1]:self.rock_position[1] + self.rock.length]
            if below_rock[i] in ['#', '-']:
                return False
        return True

    def fall(self):
        if self.fall_possible():
            for i in range(self.rock.height - 1, -1, -1):
                current_line = self.layers[self.rock_position[0] - i]
                next_line = self.layers[self.rock_position[0] - i - 1]
                new_next_line = []
                if i == self.rock.height - 1:
                    for j in range(len(current_line)):
                        if current_line[j] == '@':
                            new_next_line.append('@')
                        else:
                            new_next_line.append(next_line[j])
                else:
                    new_next_line.append('|')
                    for j in range(1, self.rock_position[1]):
                        new_next_line.append(next_line[j])
                    new_next_line.append(self.rock.shape[i])
                    for j in range(self.rock_position[1] + self.rock.length, 8):
                        new_next_line.append(next_line[j])
                    new_next_line.append('|')
                self.layers[self.rock_position[0] - i - 1] = ''.join(new_next_line)
            self.layers[self.rock_position[0]] = self.layers[self.rock_position[0]].replace('@', '.')
            self.rock_position[0] -= 1
            if self.layers[-1] == '|.......|':
                self.layers.pop()
                self.height -= 1
            # print(f'Falling')
            # self.display()
            return True
        else:
            print(f'Fall not possible - something in the way')

    def freeze(self):
        for i in range(self.rock.height):
            current_line = self.layers[self.rock_position[0] - i]
            new_line = current_line.replace('@', '#')
            for col, s in enumerate(new_line):
                if s == '#' and self.heights[col] < self.rock_position[0] - i - self.heights_subtracted:
                    self.heights[col] = self.rock_position[0] - i - self.heights_subtracted
            self.layers[self.rock_position[0] - i] = new_line
        self.rock = None
        self.rock_position = None
        self.update_heights()
        # print(f'Rock {self.rock.name} settled')
        # self.display()


def execute_moves(moves_limit):
    rocks = Rocks()
    field = Field()
    for move in range(moves_limit):
        field.add_rock(rocks.next())
        field.move(moves[field.move_count % move_modulo])
        while field.fall_possible():
            field.fall()
            field.move(moves[field.move_count % move_modulo])
        field.freeze()
    return field


def execute_moves_to_find_loop():
    rocks = Rocks()
    field = Field()
    heights_store = {}
    move = 0
    while True:
        field.add_rock(rocks.next())
        field.move(moves[field.move_count % move_modulo])
        while field.fall_possible():
            field.fall()
            field.move(moves[field.move_count % move_modulo])
        field.freeze()
        key = copy(field.heights)
        key.append(field.move_count % len(rocks.rock_supply))
        key.append(field.move_count % move_modulo)
        if tuple(key) not in heights_store:
            heights_store[tuple(key)] = [move, field.height]
        else:
            data = [heights_store[tuple(key)], [move, field.height]]
            # print(f'Heights {tuple(key)} repeat in step {heights_store[tuple(key)][0]} and step {move}')
            break
        move += 1
    return data


with open('resources/17.txt') as f:
    moves = f.read().splitlines()[0]
    move_modulo = len(moves)

# part 1
max_moves = 2022
field_1 = execute_moves(max_moves)
print(f'17a - Tower will be {field_1.height} units tall after {max_moves} rocks fall.')

# part 2
loop_data = execute_moves_to_find_loop()
max_moves = 1_000_000_000_000
diff_move = loop_data[1][0] - loop_data[0][0]
diff_height = loop_data[1][1] - loop_data[0][1]
pre_period_move = loop_data[0][1]
start_period_move = ((max_moves - pre_period_move) % diff_move) + pre_period_move
loops_count = (max_moves - pre_period_move) // diff_move
field_2 = execute_moves(start_period_move)
sol_2 = field_2.height + loops_count * diff_height
print(f'17b - Tower will be {sol_2} units tall after {max_moves} rocks fall.')
# time 8h (5+3)













