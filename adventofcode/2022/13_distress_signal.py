import ast
import functools


def extract_packet(line):
    history = []
    number = ''
    for s in line:
        if s == '[':
            history.append([])
        elif s == ']':
            if not number == '':
                history[-1].append(int(number))
                number = ''
            last = history.pop()
            if len(history) > 0:
                history[-1].append(last)
            else:
                history.append(last)
        elif s == ',':
            if number != '':
                history[-1].append(int(number))
                number = ''
        else:
            number += s
    return history[0]


def is_ordered(l1, l2):
    for n1, n2 in zip(l1, l2):
        if isinstance(n1, int) and isinstance(n2, int):
            if n1 < n2:
                return True
            elif n1 > n2:
                return False
        if isinstance(n1, list) and isinstance(n2, list):
            comp = is_ordered(n1, n2)
            if comp != None:
                return comp
        if isinstance(n1, list) and isinstance(n2, int):
            comp = is_ordered(n1, [n2])
            if comp != None:
                return comp
        if isinstance(n1, int) and isinstance(n2, list):
            comp = is_ordered([n1], n2)
            if comp != None:
                return comp
    if len(l1) < len(l2):
        return True
    elif len(l1) > len(l2):
        return False


def compare(x, y):
    return 1 if is_ordered(x, y) else -1


with open('resources/13.txt') as f:
    data = f.read().split('\n\n')

packets = []
sol_1 = []
ind = 1
for d in data:
    pair = d.splitlines()
    # packet0 = extract_packet(pair[0])
    # packet0 = eval(pair[0])
    packet0 = ast.literal_eval(pair[0])
    packets.append(packet0)
    # packet1 = extract_packet(pair[1])
    # packet1 = eval(pair[1])
    packet1 = ast.literal_eval(pair[1])
    packets.append(packet1)
    if is_ordered(packet0, packet1):
        sol_1.append(ind)
    ind += 1

packets.append(extract_packet('[[2]]'))
packets.append(extract_packet('[[6]]'))
packets_sorted = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)
ind_2 = packets_sorted.index(extract_packet('[[2]]')) + 1
ind_6 = packets_sorted.index(extract_packet('[[6]]')) + 1

print(f'13a - sum of indices of ordered pais is {sum(sol_1)}')
print(f'13b - product of positions of dividers is {ind_2 * ind_6}')
# time 4h 30m
