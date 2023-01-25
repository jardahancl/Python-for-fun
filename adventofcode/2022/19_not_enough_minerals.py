import time
from pprint import pprint
from copy import deepcopy
import dataclasses


with open('resources/19.txt') as file:
    lines = file.read().splitlines()


def get_blueprint(line):
    ln = line.split(' ')
    no_robot = [0, 0, 0, 0]
    ore_robot = [int(ln[6]), 0, 0, 0]
    clay_robot = [int(ln[12]), 0, 0, 0]
    obsidian_robot = [int(ln[18]), int(ln[21]), 0, 0]
    geode_robot = [int(ln[27]), 0, int(ln[30]), 0]
    return [ore_robot, clay_robot, obsidian_robot, geode_robot, no_robot]


@dataclasses.dataclass
class Resources:
    ore: int
    clay: int
    obsidian: int
    geode: int

    def __init__(self, ore, clay, obsidian, geode) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def as_tuple(self):
        return (self.ore, self.clay, self.obsidian, self.geode)

    def contain(self, price):
        r = self.as_tuple()
        for ind in range(len(price)):
            if r[ind] < price[ind]:
                return False
        return True

    def add(self, add_resources):
        self.ore += add_resources[0]
        self.clay += add_resources[1]
        self.obsidian += add_resources[2]
        self.geode += add_resources[3]

    def spend(self, spent_resources):
        self.add([-x for x in spent_resources])

    def smaller(self, other_resources):
        my_resources = self.as_tuple()
        for i in range(len(my_resources)):
            if my_resources[i] > other_resources[i]:
                return False
        return True


@dataclasses.dataclass
class Robots:
    ore: int
    clay: int
    obsidian: int
    geode: int

    def __init__(self, ore, clay, obsidian, geode) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def as_tuple(self):
        return (self.ore, self.clay, self.obsidian, self.geode)

    def add(self, robot_id):
        if robot_id == 0:
            self.ore += 1
        if robot_id == 1:
            self.clay += 1
        if robot_id == 2:
            self.obsidian += 1
        if robot_id == 3:
            self.geode += 1


@dataclasses.dataclass
class State:
    resources: Resources
    robots: Robots
    minute: int

    def __init__(self, resources, robots, minute) -> None:
        self.resources = resources
        self.robots = robots
        self.minute = minute

    def collect_resource(self):
        self.resources.add(self.robots.as_tuple())

    def create_robot(self, robot_id, resources_spent):
        self.resources.spend(resources_spent)
        self.robots.add(robot_id)

    def is_acceptable(self):
        if self.minute > 24 and self.robots.geode < 1:
            return False
        if self.minute > 25 and self.robots.geode < 2:
            return False
        if self.minute > 26 and self.robots.geode < 3:
            return False
        if self.minute > 27 and self.robots.geode < 4:
            return False
        if self.minute > 28 and self.robots.geode < 5:
            return False
        if self.minute > 29 and self.robots.geode < 6:
            return False
        if self.minute > 30 and self.robots.geode < 7:
            return False
        if self.minute > 31 and self.robots.geode < 8:
            return False
        return self.minute <= max_minutes


def is_incomparable_to_all(element, list_of_elements):
    for other_element in list_of_elements:
        smaller = True
        bigger = True
        for ind, x in enumerate(element):
            if x > other_element[ind]:
                smaller = False
            if x < other_element[ind]:
                bigger = False
        if smaller or bigger:
            return False
    return True


def is_above_some(element, list_of_elements):
    for other_element in list_of_elements:
        zipped = zip(element, other_element)
        if all(a >= b for a, b in zipped):
            return True
    return False


blueprints = []
for line in lines:
    blueprints.append(get_blueprint(line))
# pprint(blueprints)


result_sum = 0
max_minutes = 31
time_before = time.time()
for blueprint_number in range(1, 2):
    blueprint = blueprints[blueprint_number]
    print(blueprint)
    start_state = State(Resources(0, 0, 0, 0), Robots(1, 0, 0, 0), 0)

    best = {}
    q = [start_state]
    k = 0
    minute_stats = {}
    max_geode_resource = 0
    while len(q) > 0:
        state = q.pop(0)

        if state.minute not in minute_stats:
            minute_stats[state.minute] = 1
        else:
            minute_stats[state.minute] += 1
        for i in range(5):
            if state.resources.contain(blueprint[i]):
                new_state = deepcopy(state)
                new_state.collect_resource()
                if i < 4:
                    new_state.create_robot(i, blueprint[i])
                new_state.minute += 1
                # printing results
                if new_state.resources.geode > max_geode_resource:
                    print(f'Replacing max with {new_state} in time {time.time() - time_before}')
                    max_geode_resource = new_state.resources.geode
                # adding new results
                if new_state.is_acceptable():
                    if new_state.robots.as_tuple() not in best:
                        best[new_state.robots.as_tuple()] = [new_state.resources.as_tuple()]
                        q.append(new_state)
                    else:
                        best_list = best[new_state.robots.as_tuple()]
                        if new_state.resources.as_tuple() in best_list:
                            pass
                        elif is_above_some(new_state.resources.as_tuple(), best[new_state.robots.as_tuple()]):
                            to_remove = []
                            for best_value in best_list:
                                if all(a >= b for a, b in zip(new_state.resources.as_tuple(), best_value)):
                                    to_remove.append(best_value)
                            for best_value in to_remove:
                                best_list.remove(best_value)
                            best[new_state.robots.as_tuple()] = best_list
                            q.append(new_state)
                        elif is_incomparable_to_all(new_state.resources.as_tuple(), best[new_state.robots.as_tuple()]):
                            best_list.append(new_state.resources.as_tuple())
                            best[new_state.robots.as_tuple()] = best_list
                            q.append(new_state)
                # if state.resources.geode >= 7:
                #     print(new_state, k)
                #     k += 1

    print(minute_stats)
    print(f'Maximum geode for Blueprint {blueprint_number + 1} is {max_geode_resource}')
    result_sum += (blueprint_number + 1) * max_geode_resource
    print()

print(f'Time consumed {time.time() - time_before}')
print(f'Resulting sum is {result_sum}')
# ~15h



