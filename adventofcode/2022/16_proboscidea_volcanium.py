from pprint import pprint
from copy import deepcopy
import dataclasses


@dataclasses.dataclass
class Valve:
    name: str
    rate: int
    neighbors: list
    distances: dict

    def __init__(self, name: str, rate: str, neighbors: list) -> None:
        self.name = name
        self.rate = int(rate)
        self.neighbors = neighbors
        self.distances = {}


def update_distances(valves):
    valves_with_rate = [v[0] for v in rated_valves]
    valves_with_rate.append('AA')
    for name, valve in valves.items():
        q = []
        for n in valve.neighbors:
            q.append([n, 1])
        while len(q) > 0:
            distanced_valve = q.pop(0)
            if distanced_valve[0] not in valve.distances:
                valve.distances[distanced_valve[0]] = distanced_valve[1]
            for n in valves[distanced_valve[0]].neighbors:
                if n not in valve.distances and n != valve.name:
                    q.append([n, distanced_valve[1] + 1])
        to_remove = []
        for k in valve.distances.keys():
            if k not in valves_with_rate:
                to_remove.append(k)
        for k in to_remove:
            valve.distances.pop(k)


@dataclasses.dataclass
class State:
    path: list
    steps: list
    points: int
    visited: list

    def __init__(self, path, steps, points) -> None:
        self.path = path
        self.steps = steps
        self.points = points
        self.visited = ['AA']


def compute_tips(path, visited, steps):
    result = []
    for v in rated_valves:
        if v[0] not in visited and v[0] not in banned:
            last_valve = valves[path[-1]]
            if (steps + last_valve.distances[v[0]]) < max_steps - 1:
                result.append((v[0], v[1] - (3 * last_valve.distances[v[0]])))
    result.sort(key=lambda x: x[1], reverse=True)
    return result


def points_per_round(path):
    return sum([valves[v].rate for v in path])


# def find_max_valued_path(state):
#     if state.steps < max_steps:
#         print(state)
#         heuristics = compute_tips(state.path)
#         save_state = deepcopy(state)
#         max_state = deepcopy(state)
#
#         for t in heuristics:
#             state = deepcopy(save_state)
#
#             steps_added = min(valves[state.path[-1]].distances[t[0]] + 1, max_steps - state.steps)
#             state.steps += steps_added
#             state.points += steps_added * points_per_round(state.path)
#             state.path.append(t[0])
#
#             state = find_max_valued_path(state)
#
#             if state.points > max_state.points:
#                 max_state = deepcopy(state)
#
#         if len(heuristics) == 0:
#             max_state.points = state.points + (max_steps - state.steps) * points_per_round(state.path)
#             max_state.steps = max_steps
#
#         return max_state
#     return state


def find_max_valued_path_with_elephant(state):
    fant = 0
    if len(state.steps) > 1:
        if state.steps[0] > state.steps[1]:
            fant = 1
    if state.steps[fant] < max_steps:
        # print(fant, state)
        save_state = deepcopy(state)
        max_state = deepcopy(state)

        heuristics = compute_tips(state.path[fant], state.visited, state.steps[fant])
        for t in heuristics:
            state = deepcopy(save_state)

            steps_added = min(valves[state.path[fant][-1]].distances[t[0]] + 1, max_steps - state.steps[fant])
            state.steps[fant] += steps_added
            state.points += steps_added * points_per_round(state.path[fant])
            state.path[fant].append(t[0])
            state.visited.append(t[0])

            state = find_max_valued_path_with_elephant(state)
            if state.points > max_state.points:
                max_state = deepcopy(state)

        if len(heuristics) == 0:
            max_state.points = max_state.points + (max_steps - state.steps[fant]) * points_per_round(state.path[fant])
            max_state.steps[fant] = max_steps
            if len(state.path) > 1:
                max_state.points = max_state.points + (max_steps - state.steps[1 - fant]) * points_per_round(state.path[1 - fant])
                max_state.steps[1 - fant] = max_steps

        return max_state

    return state


with open('resources/16.txt') as f:
    lines = f.read().splitlines()

valves = {}
for line in lines:
    ln = line.split(' ')
    neigh = list(map(lambda x: x[:-1], ln[9:-1]))
    neigh.append(ln[-1])
    valves[ln[1]] = Valve(ln[1], ln[4][5:-1], neigh)
rated_valves = [(v.name, v.rate) for v in valves.values() if v.rate > 0]
rated_valves.sort(key=lambda x: x[1], reverse=True)
update_distances(valves)
# print(rated_valves)

max_steps = 30
banned = []
start_state = State([['AA']], [0], 0)
state = find_max_valued_path_with_elephant(start_state)
# print(state)
print(f'16a - one can release at most {state.points} pressure alone')


max_steps = 26
banned = []
start_state = State([['AA']], [0], 0)
result_points = [0, 0]
parity = 0
while True:
    state = find_max_valued_path_with_elephant(start_state)
    # print(state)
    banned = state.path[0][:-2]
    if result_points[parity] == state.points:
        break
    result_points[parity] = state.points
    parity = 1 - parity
print(f'16b - one can release at most {sum(result_points)} pressure using one elephant')
# time 7h