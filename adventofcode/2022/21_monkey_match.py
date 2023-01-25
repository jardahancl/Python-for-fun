import dataclasses
from pprint import pprint
from copy import deepcopy


@dataclasses.dataclass
class Monkey:
    name: str
    value: int
    waiting_for: list
    expression: str
    need_me: list

    def __init__(self, name: str, info: str) -> None:
        self.name = name
        expression = info.split(' ')
        if len(expression) == 1:
            self.value = int(expression[0])
            self.waiting_for = []
        else:
            self.value = None
            self.waiting_for = [expression[0], expression[2]]
        self.expression = info
        self.need_me = []


def evaluate_value(expression, monkeys_clone):
    exp = expression.split(' ')
    first_value = monkeys_clone[exp[0]].value
    second_value = monkeys_clone[exp[2]].value
    if exp[1] == '+':
        return first_value + second_value
    elif exp[1] == '-':
        return first_value - second_value
    elif exp[1] == '*':
        return first_value * second_value
    elif exp[1] == '/':
        return first_value // second_value
    elif exp[1] == '=':
        return first_value == second_value


with open('resources/21.txt') as file:
    lines = file.read().splitlines()

# initializing
monkeys = {}
for line in lines:
    monkey_info = line.split(':')
    monkeys[monkey_info[0]] = Monkey(monkey_info[0], monkey_info[1].strip())

# creating reverse connections via monkey.need_me
for monkey_name, monkey in monkeys.items():
    for kid_name in monkey.waiting_for:
        kid = monkeys[kid_name]
        kid.need_me.append(monkey.name)
# pprint(monkeys)

# initializing all known monkeys
q = []
for monkey_name, monkey in monkeys.items():
    if len(monkey.waiting_for) == 0:
        q.append(monkey)

# part 1
monkeys_clone = deepcopy(monkeys)
q_clone = deepcopy(q)
while len(q_clone) > 0:
    monkey = q_clone.pop(0)
    for parent_name in monkey.need_me:
        parent = monkeys_clone[parent_name]
        parent.waiting_for.remove(monkey.name)
        if len(parent.waiting_for) == 0:
            parent.value = evaluate_value(parent.expression, monkeys_clone)
            q_clone.append(parent)
print(f'21a - Monkey "root" yells {monkeys_clone["root"].value}')


def check_value(value):
    monkeys_clone = deepcopy(monkeys)
    monkeys_clone['humn'].value = value
    q_clone = deepcopy(q)
    while len(q_clone) > 0:
        monkey = q_clone.pop(0)
        for parent_name in monkey.need_me:
            parent = monkeys_clone[parent_name]
            parent.waiting_for.remove(monkey.name)
            if len(parent.waiting_for) == 0:
                if parent.name != 'root':
                    parent.value = evaluate_value(parent.expression, monkeys_clone)
                    q_clone.append(parent)
                else:
                    first_value = monkeys_clone[parent.expression.split(' ')[0]].value
                    second_value = monkeys_clone[parent.expression.split(' ')[2]].value
                    difference = first_value - second_value
                    if difference == 0:
                        pass
                        # print(f'Result is {my_value}')
                    else:
                        # print(f'For value {my_value} we have {first_value}, {second_value},  difference is {difference}')
                        return difference
    return difference

# part 2
# val = 3_715_799_488_132
decimals = -1
my_value = 1
difference = 1
while difference > 0:
    decimals += 1
    my_value *= 10
    difference = check_value(my_value)

my_value //= 10
difference = check_value(my_value)
for decimal in range(decimals, -1, -1):

    while difference > 0:
        my_value += 10 ** decimal
        difference = check_value(my_value)
    my_value -= 10 ** decimal
    difference = check_value(my_value)
print(f'21b - If you yell {my_value}, "root"s numbers will equal')
# time 3h













