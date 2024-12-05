import itertools

rules = []      # tuples of rules
rules_pre = {}  # what is before
rules_post = {} # what is after
updates = []
for line in open('resources/05.txt').read().splitlines():
    if line.__contains__('|'):
        ints = list(map(lambda x: int(x), line.split("|")))
        rules.append((ints[0], ints[1]))
        if rules_post.keys().__contains__(ints[0]):
            rules_post[ints[0]].append(ints[1])
        else:
            rules_post[ints[0]] = [ints[1]]
        if rules_pre.keys().__contains__(ints[1]):
            rules_pre[ints[1]].append(ints[0])
        else:
            rules_pre[ints[1]] = [ints[0]]
    elif line.__contains__(','):
        ints = list(map(lambda x: int(x), line.split(",")))
        updates.append(ints)


def get_min(update, rules_post):
    for ind, x in enumerate(update):
        update_without = update[:ind] + update[ind + 1:]
        if x in rules_post.keys() and set(rules_post[x]).issuperset(set(update_without)):
            return x
    return update[0]


def order_update(update, rules_post):
    result = []
    update_current = update.copy()
    for n in range(len(update)):
        min = get_min(update_current, rules_post)
        result.append(min)
        update_current.remove(min)
    return result


sum_middles_valid = 0
sum_middles_invalid = 0
for update in updates:
    update_valid = True
    for small, big in itertools.combinations(update, 2):
        if rules.__contains__((big, small)):
            update_valid = False
            break
    if update_valid:
        sum_middles_valid += update[int(len(update)/2)]
    else:
        update_ordered = order_update(update, rules_post)
        sum_middles_invalid += update_ordered[int(len(update_ordered)/2)]


print(f'05a - sum of middles in valid updates is {sum_middles_valid}')
print(f'05b - sum of middles in invalid ordered updates is {sum_middles_invalid}')
# 40m + 20m = 1h
