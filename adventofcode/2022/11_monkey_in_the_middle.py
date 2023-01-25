import math
import time


def convert_op(s):
    def d(n, xx):
        return xx if n == 'old' else int(n)
    op = s.split(' ')
    if op[1] == '+':
        return lambda x: d(op[0], x) + d(op[2], x)
    if op[1] == '*':
        return lambda x: d(op[0], x) * d(op[2], x)


def solve(m, la):
    inspections = [0 for x in range(len(items))]
    for i in range(m):
        mc = 0
        for monkey_item in items:
            for item in monkey_item:
                i = la(ops[mc](item))
                test = div_test[mc]
                if i % test[0] == 0:
                    items[test[1]].append(i)
                else:
                    items[test[2]].append(i)
                inspections[mc] += 1
            items[mc] = []
            mc += 1

    inspections.sort()
    return inspections[-2] * inspections[-1]


start_time = time.time()
with open('resources/11.txt') as f:
    lines = f.read().splitlines()

    items = []
    ops = []
    div_test = []
    monkey_count = 0
    for line in lines:
        if line.startswith('Monkey'):
            monkey_count += 1
        elif line.startswith('  Starting items:'):
            items.append([int(x) for x in line[18:].split(', ')])
        elif line.startswith('  Operation:'):
            ops.append(convert_op(line.split(' = ')[1]))
        elif line.startswith('  Test:'):
            test_info = [int(line.split(' ')[-1])]
            div_test.append(test_info)
        elif line.startswith('    If true:') or line.startswith('    If false:'):
            test_info.append(int(line.split(' ')[-1]))

    modulo = math.prod([x[0] for x in div_test])
    # sol_1 = solve(20, lambda x: x // 3)
    # print(f'11a - monkey business level is {sol_1} ')
    sol_2 = solve(10000, lambda x: x % modulo)
    print(f'11b - monkey business level is {sol_2} ')

print("--- %s seconds ---" % (time.time() - start_time))
# time 2h



