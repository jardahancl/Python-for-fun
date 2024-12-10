from queue import Queue


dirs4 = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def extend(board, n, ch):
    board_in = board.copy()
    for i in range(n):
       for l in range(len(board_in)):
           board_in[l] = ch + board_in[l] + ch
       board_in = [ch * len(board_in[0])] + board_in + [ch * len(board_in[0])]
    return board_in


board = []
for line in open('resources/10.txt').read().splitlines():
    board.append(line)
mapa = extend(board, 1, '.')


zeros = []
for l in range(len(mapa)):
    for c in range(len(mapa[l])):
        if mapa[l][c] == '0':
            zeros.append((l, c))


def count_trails(line, col):
    visited_counts = {(line, col): 1}
    q = Queue()
    q.put((line, col))
    while not q.empty():
        curr = q.get()
        next_s = str(int(mapa[curr[0]][curr[1]]) + 1)
        for d in dirs4:
            next_pos = (curr[0] + d[0], curr[1] + d[1])
            if mapa[next_pos[0]][next_pos[1]] == next_s:
                if not visited_counts.keys().__contains__(next_pos):
                    q.put(next_pos)
                if visited_counts.keys().__contains__(next_pos):
                    visited_counts[next_pos] = visited_counts[next_pos] + visited_counts[curr]
                else:
                    visited_counts[next_pos] = visited_counts[curr]
    visited_9 = [x for x in visited_counts.keys() if mapa[x[0]][x[1]] == '9']
    visited_rating_9 = [visited_counts[x] for x in visited_counts.keys() if mapa[x[0]][x[1]] == '9']
    return len(visited_9), sum(visited_rating_9)


trailhead_sum = 0
trailhead_rating_sum = 0
for line, col in zeros:
    trailhead_count, trailhead_rating_count = count_trails(line, col)
    trailhead_sum += trailhead_count
    trailhead_rating_sum += trailhead_rating_count


print(f'10a - trailhead sum is {trailhead_sum}')
print(f'10a - trailhead rating sum is {trailhead_rating_sum}')
# 35m + 40m = 1h 15m