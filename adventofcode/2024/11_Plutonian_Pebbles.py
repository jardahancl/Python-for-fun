pebbles = []
cache = {}
for line in open('resources/11.txt').read().splitlines():
    pebbles = list(map(lambda x: int(x), line.split(" ")))


def evolve_v1(stones, steps):
    for i in range(steps):
        stones_next = []
        for stone in stones:
            if stone == 0:
                stones_next.append(1)
            elif len(str(stone)) % 2 == 0:
                stones_next.append(int(str(stone)[:int(len(str(stone))/2)]))
                stones_next.append(int(str(stone)[int(len(str(stone))/2):]))
            else:
                stones_next.append(stone * 2024)
        stones = stones_next
    return len(stones)


def evolve_v2(stone, steps, cache):
    if not cache.keys().__contains__(stone):
        descendants = [stone * 2024]
        if stone == 0:
            descendants = [1]
        elif len(str(stone)) % 2 == 0:
            descendants = [int(str(stone)[:int(len(str(stone)) / 2)]), int(str(stone)[int(len(str(stone)) / 2):])]
        cache[stone] = [descendants, {0: 1}]
    if not cache[stone][1].keys().__contains__(steps):
        cache[stone][1][steps] = sum([evolve_v2(x, steps - 1, cache) for x in cache[stone][0]])
    return cache[stone][1][steps]


count_v1 = evolve_v1(pebbles.copy(), 25)
count_v2 = sum([evolve_v2(p, 75, cache) for p in pebbles])

print(f'11a - after 25 evolutions we have {count_v1} pebbles')
print(f'11b - after 75 evolutions we have {count_v2} pebbles')
# 20m + 2h
