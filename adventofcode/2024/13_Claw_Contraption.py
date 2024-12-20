import re
from collections import namedtuple
import math
from sympy import symbols, Eq, solve


problem_nr = __file__.split("\\")[-1][0:2]
machines = []
machines_v2 = []
Machine = namedtuple('Machine', ['a', 'b', 'prize'])
CC = namedtuple('CC', ['x', 'y'])
for line in open(f'resources/{problem_nr}.txt').read().split("\n\n"):
    numbers = list(map(lambda x: int(x), re.findall(r"\d+", line)))
    a = CC(numbers[0], numbers[1])
    b = CC(numbers[2], numbers[3])
    prize = CC(numbers[4], numbers[5])
    machines.append(Machine(a, b, prize)) # 10 000 000 000 000
    prize_v2 = CC(numbers[4] + 10_000_000_000_000, numbers[5] + 10_000_000_000_000)
    machines_v2.append(Machine(a, b, prize_v2))

prizeA = 3
prizeB = 1


def get_min_sol(a, b, p):
    lcm = math.lcm(a, b)
    gdc = math.gcd(a, b)
    if p % gdc != 0:
        return False, None
    p_div = int(p / lcm)
    p_res = p - (p_div * lcm)
    sol = ()
    for i in range(int(b / gdc)):
        if (p_res - (i * a)) % b == 0:
            sol = (i, int((p_res - (i * a)) / b))
            break
    if not sol or sol[0] < 0 or sol[1] < 0:
        for i in range(int(b / gdc)):
            if (p_res + lcm - (i * a)) % b == 0:
                sol = (i, int((p_res + lcm - (i * a)) / b))
                break
    return True, sol


def eval_machine(m, eval_max):
    solutions = []
    for i in range(eval_max+1):
        if (m.prize.x - (i * m.a.x)) % m.b.x == 0 and (m.prize.y - (i * m.a.y)) % m.b.y == 0:
            x_res = int((m.prize.x - (i * m.a.x)) / m.b.x)
            y_res = int((m.prize.y - (i * m.a.y)) / m.b.y)
            if x_res == y_res and 0 <= x_res <=  eval_max:
                solutions.append([i, x_res])
                break
    if not solutions:
        return 0
    min_solution = min([sol[0] * prizeA + sol[1] * prizeB  for sol in solutions])
    # print(min_solution)
    return min_solution


def get_part1(ms, eval_max):
    return sum([eval_machine(m, eval_max) for m in ms])


def eval_machine_v2(m):
    u, v = symbols("u v", integer=True)
    eq1 = Eq(m.a.x * u + m.b.x * v, m.prize.x)
    eq2 = Eq(m.a.y * u + m.b.y * v, m.prize.y)

    solutions = solve((eq1, eq2), (u, v))

    return solutions[u] * prizeA + solutions[v] * prizeB if len(solutions) > 0 else 0


def get_part2(ms):
    return sum([eval_machine_v2(m) for m in ms])


part1 = get_part1(machines, 100)
# part1 = get_part2(machines)
part2 = get_part2(machines_v2)
print(f'13a - result of part1 is {part1}')
print(f'13b - result of part2 is {part2}')
# 1h 20m + 1h




