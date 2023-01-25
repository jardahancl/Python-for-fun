import copy

with open('resources/05.txt', mode='r') as f:
    def create_stocks(n, start):
        result = [[] for _ in range(n)]
        for count in range(n):
            for size in range(len(start)):
                if len(start[len(start) - 1 - size]) >= (1 + 4*count) and start[len(start) - 1 - size][1 + 4*count] != ' ':
                        result[count].append(start[len(start) - 1 - size][1 + 4*count])
                else:
                    break
        return result

    def execute_by_one(stocks_1, inst):
        for i in range(inst[0]):
            s = stocks_1[inst[1]-1].pop()
            stocks_1[inst[2]-1].append(s)

    def execute_by_size(stocks_2, inst):
        s = []
        for i in range(inst[0]):
            s.append(stocks_2[inst[1]-1].pop())
        s.reverse()
        stocks_2[inst[2]-1].extend(s)

    data = f.read().splitlines()

    starting_position = []
    instructions = []
    for line in data:
        if line.startswith('  ') or line.startswith('['):
            starting_position.append(line)
        elif line.startswith(' 1'):
            stock_number = int(line.split('  ')[-1].strip())
        elif line.startswith('move'):
            instructions.append(list(map(int, line.split(' ')[1::2])))

    stocks = create_stocks(stock_number, starting_position)
    stocks_1 = copy.deepcopy(stocks)
    stocks_2 = copy.deepcopy(stocks)

    for inst in instructions:
        execute_by_one(stocks_1, inst)
        execute_by_size(stocks_2, inst)

    solution_1 = ''.join(list(map(lambda x: x[-1], stocks_1)))
    solution_2 = ''.join(list(map(lambda x: x[-1], stocks_2)))

    print('Starting position ' + ''.join(list(map(lambda x: x[-1], stocks))))
    print(f'05a - after moving by one {solution_1}')
    print(f'05b - bfter moving by many {solution_2}')
    # time 1h 15m



