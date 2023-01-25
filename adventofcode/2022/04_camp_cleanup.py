def range_contained(x):
    first_set = set(range(int(x[0][0]), int(x[0][1]) + 1))
    second_set = set(range(int(x[1][0]), int(x[1][1]) + 1))
    return first_set.issubset(second_set) or first_set.issuperset(second_set)


def range_intersected(x):
    first_set = set(range(int(x[0][0]), int(x[0][1]) + 1))
    second_set = set(range(int(x[1][0]), int(x[1][1]) + 1))
    return not first_set.isdisjoint(second_set)


with open('resources/04.txt', mode='r') as f:
    data = f.read().splitlines()

    splitted = list(map(lambda x: str(x).split(','), data))
    in_list = list(map(lambda x: [str(x[0]).split('-'), str(x[1]).split('-')], splitted))

    result_1 = list(map(range_contained, in_list))
    result_2 = list(map(range_intersected, in_list))

    print(f'04a - {sum(result_1)}')
    print(f'04b - {sum(result_2)}')
    # time 40m
