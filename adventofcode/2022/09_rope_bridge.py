def move_head(direction, s):
    if direction == 'L':
        s[0][0] -= 1
    elif direction == 'R':
        s[0][0] += 1
    elif direction == 'D':
        s[0][1] -= 1
    elif direction == 'U':
        s[0][1] += 1


def move_tail(s):
    for t in range(1, len(s)):
        diff = [x - y for x, y in zip(s[t-1], s[t])]
        rad = sum([abs(x) for x in diff])
        for d in range(2):
            if abs(diff[d]) == 2:
                s[t][d] += diff[d] // 2
            elif abs(diff[d]) == 1 and rad == 3:
                s[t][d] += diff[d]
    return s


with open('resources/09.txt') as f:
    lines = f.read().splitlines()

    snake = [[0, 0] for i in range(10)]
    last_tail_visited = set()
    first_tail_visited = set()
    for line in lines:
        ln = line.split(' ')
        for step in range(int(ln[1])):
            move_head(ln[0], snake)
            move_tail(snake)
            first_tail_visited.add(tuple(snake[1]))
            last_tail_visited.add(tuple(snake[-1]))

    print(f'09a - second tail visited {len(first_tail_visited)} positions')
    print(f'09b - last tail visited {len(last_tail_visited)} positions')
    # time 2h
