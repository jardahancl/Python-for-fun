def print_result(c, v):
    if c % 40 in range(v, (v + 3)):
        print('#', end=' ')
    else:
        print('.', end=' ')
    if c % 40 == 0:
        print('')


with open('resources/10.txt') as f:
    lines = f.read().splitlines()

    value = 1
    cycle = 0
    strength = []
    for line in lines:
        if line.startswith('noop'):
            cycle += 1
            if cycle % 40 == 20:
                strength.append([cycle, value])
            print_result(cycle, value)
        else:
            for i in range(2):
                cycle += 1
                if cycle % 40 == 20:
                    strength.append([cycle, value])
                print_result(cycle, value)
            value += int(line.split(' ')[1])

    result_a = sum([x[0] * x[1] for x in strength])
    print(f'10a - sum of interesting signal strength is {result_a}')
    print(f'10b - solution is displayed above')
    # time 1h 20m


