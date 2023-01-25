def start(n):
    result = []
    for i in range(n):
        result.append(1)
    return result

def update(hits, side_count):
    prehits = []
    for i in range(side_count-1):
        prehits.    append(0)
    prehits.extend(hits)
    #print(prehits)

    result = []
    for i in range(len(prehits)):
        to_add = sum(prehits[i:i+side_count])
        result.append(to_add)
    # for i in range(len(hits)):
    return result

def convert(hits, dice_count):
    result = []
    for i in range(len(hits)):
        result.append([dice_count + i, hits[i]])
    return result

def reg_sum_hits(dice_count, side_count):
    hits = start(side_count)
    for i in range(dice_count - 1):
        print(hits)
        hits = update(hits, side_count)
    return convert(hits, dice_count)

print(reg_sum_hits(3, 4))