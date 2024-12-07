import itertools
from dataclasses import dataclass


@dataclass
class Rule:
    sum: int
    ints: list[int]


rules = []
for line in open('resources/07.txt').read().splitlines():
    vals = list(map(lambda x:int(x), line.split(" ")[1:]))
    rules.append(Rule(int(line.split(":")[0]), vals))
    # if len(vals) < 2:
    #     print("error")

print(rules[0])
calibration_sum = 0


def calculate(current_sum, total_sum, numbers):
    if len(numbers) == 0:
        return current_sum == total_sum
    res_plus = calculate(current_sum + numbers[0], total_sum, numbers[1:])
    res_prod = calculate(current_sum * numbers[0], total_sum, numbers[1:])
    concat = int(str(current_sum) + str(numbers[0]))
    res_concat = calculate(concat, total_sum, numbers[1:])
    return any([res_plus, res_prod, res_concat])

for rule in rules:
    if calculate(rule.ints[0], rule.sum, rule.ints[1:]):
        calibration_sum += rule.sum

print(f'07a - calibration sum is {calibration_sum}')
# print(f'07b - sum of middles in invalid ordered updates is {sum_middles_invalid}')
# 25m + 5m