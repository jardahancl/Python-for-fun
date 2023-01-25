with open('resources/18.txt') as file:
    lines = file.read().splitlines()


def is_in_range(x, range_min, range_max):
    for coord in range(len(x)):
        if x[coord] < range_min - 1 or x[coord] > range_max + 1:
            return False
    return True


cubes = []
for line in lines:
    cubes.append(list(map(int, line.split(','))))

faces_not_covered = 0
for c in cubes:
    for vx, vy, vz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
        if [c[0] + vx, c[1] + vy, c[2] + vz] not in cubes:
            faces_not_covered += 1
print(f'18a - there are {faces_not_covered} faces not covered')


size_max = max([max([x[0], x[1], x[2]]) for x in cubes])
size_min = min([min([x[0], x[1], x[2]]) for x in cubes])
print(f'Size is from {size_min} to {size_max}')
start = [size_min - 1, size_min - 1, size_min - 1]
board = {}
for x in range(size_min - 1, size_max + 2):
    for y in range(size_min - 1, size_max + 2):
        for z in range(size_min - 1, size_max + 2):
            board[(x, y, z)] = False

q = [start]
board[tuple(start)] = True
while len(q) > 0:
    b = q.pop()
    for vx, vy, vz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
        n = [b[0] + vx, b[1] + vy, b[2] + vz]
        if is_in_range(n, size_min, size_max):
            if n not in cubes:
                if not board[tuple(n)]:
                    q.append(n)
                board[tuple(n)] = True

faces_visible = 0
for c in cubes:
    for vx, vy, vz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
        n = [c[0] + vx, c[1] + vy, c[2] + vz]
        if is_in_range(n, size_min, size_max):
            if n not in cubes and board[tuple(n)]:
                faces_visible += 1
print(f'18b - there are {faces_visible} visible from outdoor')  # 2009 too low
# time 1h 30m

