dirs4 = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dirsX = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
dirs8 = dirs4 + dirsX


def extend(board, n, ch):
    board_in = board.copy()
    for i in range(n):
       for l in range(len(board_in)):
           board_in[l] = ch + board_in[l] + ch
       board_in = [ch * len(board_in[0])] + board_in + [ch * len(board_in[0])]
    return board_in


