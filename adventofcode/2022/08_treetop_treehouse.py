def count_direction_scenic(a, v):
    count = 0
    for i in range(len(a)):
        count += 1
        if a[i] >= v:
            return count
    return count


def count_scenic_number(left, right, up, down, value):
    result = count_direction_scenic(list(reversed(left)), value)
    result *= count_direction_scenic(right, value)
    result *= count_direction_scenic(list(reversed(up)), value)
    result *= count_direction_scenic(down, value)
    return result


with open('resources/08.txt') as f:
    lines = f.read().splitlines()

    n = len(lines)
    visible_sum = 4*n - 4
    max_scenic = 0
    columns = list(zip(*lines))
    for row in range(1, n-1):
        for col in range(1, n-1):
            left = [int(k) for k in lines[row][0:col]]
            right = [int(k) for k in lines[row][col + 1:]]
            up = [int(k) for k in columns[col][0:row]]
            down = [int(k) for k in columns[col][row + 1:]]

            height = int(lines[row][col])
            if min(max(left), max(right), max(up), max(down)) < height:
                visible_sum += 1
            current_scenic = count_scenic_number(left, right, up, down, height)
            if current_scenic > max_scenic:
                max_scenic = current_scenic
    print(f'08a - Sum of visible trees: {visible_sum}')
    print(f'08b - Max scenic number: {max_scenic}')
    # time 2h
