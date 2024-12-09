from dataclasses import dataclass

@dataclass
class Block:
    len: int
    id: int


def multiply(n, m):
    # print(n, m)
    return int(n * m)


hdd = []
for line in open('resources/09.txt').read().splitlines():
    for x in line:
        hdd.append(int(x))


checksum = 0
pos = 0
ind_left = 0
left_count = hdd[ind_left]
ind_right = len(hdd) - 1 if (len(hdd) - 1) % 2 == 0 else len(hdd) - 2
right_count = hdd[ind_right]
while ind_left < ind_right or (ind_left == ind_right and right_count > 0):
    if ind_left == ind_right:
        checksum += multiply(int(ind_right / 2), pos)
        pos += 1
        right_count -= 1
    elif ind_left % 2 == 0:
        for i in range(left_count):
            checksum += multiply(int(ind_left / 2), pos)
            pos += 1
        ind_left += 1
        left_count = hdd[ind_left]
    else:
        if left_count == 0:
            ind_left += 1
            left_count = hdd[ind_left]
        elif right_count == 0:
            ind_right -= 2
            right_count = hdd[ind_right]
        else:
            checksum += multiply(int(ind_right / 2), pos)
            pos += 1
            right_count -= 1
            left_count -= 1


hdd_blocks = []
id = 0
for ind, x in enumerate(hdd):
    if ind % 2 != 0:
        hdd_blocks.append(Block(x, -1))
    else:
        hdd_blocks.append(Block(x, id))
        id += 1


hdd_comprimed = hdd_blocks.copy()
moving_ind = len(hdd_comprimed) - 1
while moving_ind > 0:
    if hdd_comprimed[moving_ind].id != -1:
        moving_block = hdd_comprimed[moving_ind]
        vacant_ind = 0
        while vacant_ind < moving_ind:
            vacant_block = hdd_comprimed[vacant_ind]
            if (vacant_block.len >= moving_block.len) and (vacant_block.id == -1):
                if vacant_block.len == moving_block.len:
                    hdd_comprimed[vacant_ind] = Block(moving_block.len, moving_block.id)
                    hdd_comprimed[moving_ind] = Block(moving_block.len, -1)
                else:
                    vacant_part1 = Block(moving_block.len, moving_block.id)
                    vacant_part2 = Block(vacant_block.len - moving_block.len, vacant_block.id)
                    moving_new = Block(moving_block.len, -1)
                    hdd_comprimed = hdd_comprimed[:vacant_ind] + [vacant_part1] + [vacant_part2] + hdd_comprimed[vacant_ind+1:moving_ind] + [moving_new] + hdd_comprimed[moving_ind+1:]
                    moving_ind += 1
                vacant_ind += 1
                break
            vacant_ind += 1
        moving_ind -= 1
    else:
        moving_ind -= 1


checksum_block = 0
pos = 0
for i, b in enumerate(hdd_comprimed):
    if b.id != -1:
        for x in range(b.len):
            checksum_block += multiply(b.id, pos)
            pos += 1
    else:
        pos += b.len


print(f'09a - filesystem checksum is {checksum}')
print(f'09b - block checksum is {checksum_block}')
# 1h + 1h 30m