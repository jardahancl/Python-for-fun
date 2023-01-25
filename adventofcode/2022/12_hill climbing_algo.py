from queue import Queue


def add_neighbour(c, n, q):
    def inside(point):
        if point[0] < 0 or point[0] >= shape[0]:
            return False
        if point[1] < 0 or point[1] >= shape[1]:
            return False
        return True

    def possible_step(c, n):
        if ord(board[n[0]][n[1]]) - ord(board[c[0]][c[1]]) <= 1 and board[n[0]][n[1]] != 'E':
            return True
        if board[c[0]][c[1]] == 'z' and board[n[0]][n[1]] == 'E':
            return True
        return False

    if inside(n) and possible_step(c, n):
        q.put([n[0], n[1], c[2] + 1])


def shortest_path(start):
    visited = {}
    q = Queue()
    for st in start:
        q.put(st)
    while not q.empty():
        curr = q.get()
        if (curr[0], curr[1]) not in visited:
            visited[(curr[0], curr[1])] = curr[2]
            if board[curr[0]][curr[1]] == 'E':
                return curr[2]
            add_neighbour(curr, [curr[0] + 1, curr[1]], q)
            add_neighbour(curr, [curr[0] - 1, curr[1]], q)
            add_neighbour(curr, [curr[0], curr[1] + 1], q)
            add_neighbour(curr, [curr[0], curr[1] - 1], q)


with open('resources/12.txt') as f:
    lines = f.read().splitlines()

board = []
start_S = []
start_a = []
for line in lines:
    ln = list(line)
    for i in range(len(ln)):
        if ln[i] == 'S':
            start_S.append([len(board), i, 0])
            ln[i] = 'a'
        if ln[i] == 'a':
            start_a.append([len(board), i, 0])
    board.append(ln)
shape = [len(board), len(board[0])]

sol_1 = shortest_path(start_S)
print(f'12a - it takes {sol_1} steps to get from S to the E')
sol_2 = shortest_path(start_a)
print(f'12b - it takes {sol_2} steps to get from a to the E')
# time 2h 30m



