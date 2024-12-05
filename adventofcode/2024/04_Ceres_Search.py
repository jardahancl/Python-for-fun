dirs4 = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dirsX = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
dirs8 = dirs4 + dirsX


def extend(board, n):
    board_in = board.copy()
    for i in range(n):
       for l in range(len(board_in)):
           board_in[l] = '.' + board_in[l] + '.'
       board_in = ['.' * len(board_in[0])] + board_in + ['.' * len(board_in[0])]
    return board_in


def count_from(board_ex, line, col, pattern):
    count = 0
    for d in dirs8:
        if count_from_dir(board_ex, line, col, pattern, d):
            count += 1
    return count


def count_from_dir(board_ex, line, col, pattern, dir):
    count_sum = 0
    for str_ind in range(len(pattern)):
        if board_ex[line + str_ind * dir[0]][col + str_ind * dir[1]] == pattern[str_ind]:
            if str_ind == len(pattern) - 1:
                count_sum += 1
        else:
            break
    return count_sum == 1


def count_from_dir_all(board_ex, line, col, parameters):
    res = [count_from_dir(board_ex, line, col, par[0], par[1]) for par in parameters]
    return all(res)


count_XMAS = 0
count_X_MAS = 0
board = []
for line in open('resources/04.txt').read().splitlines():
    board.append(line)

board_ex = extend(board, 3)
for l in range(len(board_ex)):
    print(board_ex[l])
for l in range(3, len(board_ex) - 3):
    for c in range(3, len(board_ex[0]) - 3):
        if board_ex[l][c] == 'X':
            count_XMAS += count_from(board_ex, l, c, 'XMAS')
for l in range(3, len(board_ex) - 3):
    for c in range(3, len(board_ex[0]) - 3):
        if board_ex[l][c] == 'A':
            par = [['AM', [-1, -1]], ['AM', [1, -1]], ['AS', [1, 1]], ['AS', [-1, 1]]]
            if count_from_dir_all(board_ex, l, c, par):
                count_X_MAS += 1
            par = [['AS', [-1, -1]], ['AM', [1, -1]], ['AM', [1, 1]], ['AS', [-1, 1]]]
            if count_from_dir_all(board_ex, l, c, par):
                count_X_MAS += 1
            par = [['AS', [-1, -1]], ['AS', [1, -1]], ['AM', [1, 1]], ['AM', [-1, 1]]]
            if count_from_dir_all(board_ex, l, c, par):
                count_X_MAS += 1
            par = [['AM', [-1, -1]], ['AS', [1, -1]], ['AS', [1, 1]], ['AM', [-1, 1]]]
            if count_from_dir_all(board_ex, l, c, par):
                count_X_MAS += 1


print(f'04a - XMAS count is {count_XMAS}')
print(f'04b - X-MAS count is {count_X_MAS}')
# 1h + 45m
