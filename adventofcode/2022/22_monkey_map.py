from collections import namedtuple
from pprint import pprint


Point = namedtuple('Point', 'row, col')
Position = namedtuple('Position', 'row, col, dir')
Instruction = namedtuple('Instruction', 'step, dir')
Jump = namedtuple('Jump', 'start, end')


with open('resources/22.txt') as file:
    chunks = file.read().split('\n\n')

# initialization from input
map = []
row_jumps = [Jump(0, 0)]
col_jumps = [Jump(0, 0)]
max_map_len = max([len(ln) for ln in chunks[0].splitlines()]) + 2
map.append('X' * max_map_len)
for line in chunks[0].splitlines():
    line_map = ('X' + line)
    first_index_used = line_map.rfind(' ') + 1 if line_map.rfind(' ') != -1 else 1
    last_index_used = len(line_map) - 1
    row_jumps.append(Jump(first_index_used, last_index_used))
    line_map = line_map.replace(' ', 'X') + ('X' * (max_map_len - len(line_map)))
    map.append(line_map)
map.append('X' * max_map_len)
for col in range(1, len(map[0]) - 1):
    map_exist = [i for i in range(len(map)) if map[i][col] != 'X']
    col_jumps.append(Jump(map_exist[0], map_exist[-1]))
# print(map)
# print(row_jumps)
# print(col_jumps)

cube_jumps = {}
for i in range(1, 51):
    # A -> D
    jump_start = Position(i, 51, '<')
    jump_end = Position(151 - i, 1, '>')
    cube_jumps[jump_start] = jump_end
    # D -> A
    jump_start = Position(151 - i, 1, '<')
    jump_end = Position(i, 51, '>')
    cube_jumps[jump_start] = jump_end

    # A -> F
    jump_start = Position(1, 50 + i, '^')
    jump_end = Position(150 + i, 1, '>')
    cube_jumps[jump_start] = jump_end
    # F -> A
    jump_start = Position(150 + i, 1, '<')
    jump_end = Position(1, 50 + i, 'v')
    cube_jumps[jump_start] = jump_end

    # C -> D
    jump_start = Position(50 + i, 51, '<')
    jump_end = Position(101, i, 'v')
    cube_jumps[jump_start] = jump_end
    # D -> C
    jump_start = Position(101, i, '^')
    jump_end = Position(50 + i, 51, '>')
    cube_jumps[jump_start] = jump_end

    # B -> F
    jump_start = Position(1, 100 + i, '^')
    jump_end = Position(200, i, '^')
    cube_jumps[jump_start] = jump_end
    # F -> B
    jump_start = Position(200, i, 'v')
    jump_end = Position(1, 100 + i, 'v')
    cube_jumps[jump_start] = jump_end

    # E -> F
    jump_start = Position(150, 50 + i, 'v')
    jump_end = Position(150 + i, 50, '<')
    cube_jumps[jump_start] = jump_end
    # F -> E
    jump_start = Position(150 + i, 50, '>')
    jump_end = Position(150, 50 + i, '^')
    cube_jumps[jump_start] = jump_end

    # E -> B
    jump_start = Position(151 - i, 100, '>')
    jump_end = Position(i, 150, '<')
    cube_jumps[jump_start] = jump_end
    # B -> E
    jump_start = Position(i, 150, '>')
    jump_end = Position(151 - i, 100, '<')
    cube_jumps[jump_start] = jump_end

    # C -> B
    jump_start = Position(50 + i, 100, '>')
    jump_end = Position(50, 100 + i, '^')
    cube_jumps[jump_start] = jump_end
    # B -> C
    jump_start = Position(50, 100 + i, 'v')
    jump_end = Position(50 + i, 100, '<')
    cube_jumps[jump_start] = jump_end


instructions = []
number = ''
for st in chunks[1]:
    if st.isnumeric():
        number += st
    else:
        instructions.append(Instruction(int(number), st))
        number = ''
# instructions.append(Instruction(int(number), 'hold'))
# print(instructions)
# print(f'Max step is {max([inst.step for inst in instructions])}')
# print(len(instructions))


def move_line(line, jump, actual, direction, step):
    for i in range(step):
        if direction == '+':
            if line[actual + 1] == '.':
                actual += 1
            elif line[actual + 1] == 'X':
                if line[jump.start] == '.':
                    actual = jump.start
                elif line[jump.start] == '#':
                    return actual
            elif line[actual + 1] == '#':
                return actual
        elif direction == '-':
            if line[actual - 1] == '.':
                actual -= 1
            elif line[actual - 1] == 'X':
                if line[jump.end] == '.':
                    actual = jump.end
                elif line[jump.end] == '#':
                    return actual
            elif line[actual - 1] == '#':
                return actual
    return actual


def move(position: Position, step):
    result_row = position.row
    result_col = position.col
    if position.dir == '>':
        result_col = move_line(map[position.row], row_jumps[position.row],  position.col, '+', step)
    elif position.dir == '<':
        result_col = move_line(map[position.row], row_jumps[position.row], position.col, '-', step)
    elif position.dir == 'v':
        actual_line = ''.join([map[xx][position.col] for xx in range(len(map))])
        result_row = move_line(actual_line, col_jumps[position.col], position.row, '+', step)
    elif position.dir == '^':
        actual_line = ''.join([map[xx][position.col] for xx in range(len(map))])
        result_row = move_line(actual_line, col_jumps[position.col], position.row, '-', step)
    return result_row, result_col


def cube_move(position: Position, step):
    result_row = position.row
    result_col = position.col
    result_dir = position.dir
    for _ in range(step):
        if Position(result_row, result_col, result_dir) in cube_jumps:
            next_position = cube_jumps[Position(result_row, result_col, result_dir)]
            if map[next_position.row][next_position.col] == '#':
                return result_row, result_col, result_dir
            else:
                result_row = next_position.row
                result_col = next_position.col
                result_dir = next_position.dir
        elif result_dir == '>':
            result_col = move_line(map[result_row], None, result_col, '+', 1)
        elif result_dir == '<':
            result_col = move_line(map[result_row], None, result_col, '-', 1)
        elif result_dir == 'v':
            actual_line = ''.join([map[xx][result_col] for xx in range(len(map))])
            result_row = move_line(actual_line, None, result_row, '+', 1)
        elif result_dir == '^':
            actual_line = ''.join([map[xx][result_col] for xx in range(len(map))])
            result_row = move_line(actual_line, None, result_row, '-', 1)

    return result_row, result_col, result_dir


def turn(turn_direction):
    if turn_direction == 'R':
        return (directions_position + 1) % 4
    elif turn_direction == 'L':
        return (directions_position - 1) % 4
    return directions_position


directions = '>v<^'
directions_position = 0
start = [1, 51]

# part 1
current_position = Position(start[0], start[1], '>')
for ins in instructions:
    row, col = move(current_position, ins.step)
    directions_position = turn(ins.dir)
    current_position = Position(row, col, directions[directions_position])
sol_1 = 1000 * current_position.row + 4 * current_position.col + directions_position
print(f'20a - password for straight moving is {sol_1}')


# part 2
current_position = Position(start[0], start[1], '>')
# print(current_position)
for ins in instructions:
    # print(ins)
    row, col, dir = cube_move(current_position, ins.step)
    directions_position = directions.index(dir)
    directions_position = turn(ins.dir)
    current_position = Position(row, col, directions[directions_position])
    # print(current_position)
sol_2 = 1000 * current_position.row + 4 * current_position.col + directions_position
print(f'20b - password for cube moving is {sol_2}')  # 95291
# time 5h





