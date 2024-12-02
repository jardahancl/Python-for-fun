# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

safe_count = 0
less_safe_count = 0


def is_safe(vals):
    diffs = [y - x for x, y in zip(vals, vals[1:])]
    cond1 = (abs(sum(diffs)) == sum([abs(x) for x in diffs]))
    cond2_list = [0 < abs(x) < 4 for x in diffs]
    cond2 = (sum(cond2_list) == len(cond2_list))
    return cond1 and cond2


def is_save_v2():
    cond_list = []
    for i in range(len(vals)):
        vals_v2 = vals[:i] + vals[i + 1:]
        cond_list.append(is_safe(vals_v2))
    return any(cond_list)


for line in open('resources/02.txt').read().splitlines():
    vals = [int(t) for t in list(line.split(" "))]

    if is_safe(vals):
        safe_count += 1

    if is_save_v2(vals):
        less_safe_count += 1



print(f'01a - safe count is {safe_count}')
print(f'01b - less safe count is {less_safe_count}')
# 15m + 45m