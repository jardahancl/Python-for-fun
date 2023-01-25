from pprint import pprint
import dataclasses


def get_input(lns):
    ss = []
    bs = []
    for line in lns:
        ln = line.split(' ')
        ss.append(Sensor(int(ln[2][2:-1]), int(ln[3][2:-1]), int(ln[8][2:-1]), int(ln[9][2:])))
        beacon = [int(ln[8][2:-1]), int(ln[9][2:])]
        if beacon not in bs:
            bs.append(beacon)
    return ss, bs


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


@dataclasses.dataclass
class Sensor:
    x: int
    y: int
    x_closest_beacon: int
    y_closest_beacon: int

    @property
    def no_beacon_dist(self) -> int:
        return abs(self.x - self.x_closest_beacon) + abs(self.y - self.y_closest_beacon)

    def is_in_range(self, x_other, y_other) -> bool:
        return dist(self.x, self.y, x_other, y_other) <= self.no_beacon_dist

    def get_x_start_range_in_line(self, y_line) -> int:
        return self.x - (self.no_beacon_dist - abs(self.y - y_line))

    def get_x_end_range_in_line(self, y_line) -> int:
        return self.x + (self.no_beacon_dist - abs(self.y - y_line))


with open('resources/15.txt') as f:
    lines = f.read().splitlines()

sensors, beacons = get_input(lines)
range_sensors = [[min([s.x - s.no_beacon_dist for s in sensors]), max([s.x + s.no_beacon_dist for s in sensors])],
                 [min([s.y - s.no_beacon_dist for s in sensors]), max([s.x + s.no_beacon_dist for s in sensors])]]

y = 2000000
sol_1 = max(s.get_x_end_range_in_line(y) for s in sensors) - \
        min(s.get_x_start_range_in_line(y) for s in sensors) + 1
for b in beacons:
    if b[1] == y:
       sol_1 -= 1
print(f'15a - there are {sol_1} positions that cannot contain beacon on line {y}')

range_beacon_search = 4000000
for y in range(range_beacon_search):
    x = 0
    while x <= range_beacon_search:
        x_new = x
        for s in sensors:
            if s.is_in_range(x, y):
                x_new = s.get_x_end_range_in_line(y) + 1
                break
        if x == x_new:
            sol_2 = x * 4000000 + y
            break
        x = x_new
print(f'15b - tuning frequency is {sol_2}')
# time 3h

