sums = []
local_sum = 0
for line in open('resources/01.txt').read().splitlines():
    if len(line) > 1:
        local_sum += int(line)
    else:
        sums.append(local_sum)
        local_sum = 0
sums.sort()

print(f'01a - top 1 sum is {sums[-1]}')
print(f'01b - top 3 sum is {sum(sums[-3:])}')
# time 30m

