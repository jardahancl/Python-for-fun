import re


sum = 0
sum_v2 = 0
enabled = True


def getSumOfMuls(line):
    linesum = 0
    match = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
    for m in match:
        ints = re.findall(r"\d{1,3}", m)
        linesum += int(ints[0]) * int(ints[1])
    return linesum


for line in open('resources/03.txt').read().splitlines():
    sum += getSumOfMuls(line)

    parts = line.split("do()")
    for index, part in enumerate(parts):
        miniparts = part.split("don't()")
        if enabled or index > 0:
            sum_v2 += getSumOfMuls(miniparts[0])
        enabled = not (len(miniparts) > 1)


print(f'03a - sum is {sum}')
print(f'03b - en/dis-abled sum is {sum_v2}')
# 25m + 1h = 1h 25m
