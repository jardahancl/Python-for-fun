with open('resources/06.txt', mode='r') as f:
    def different(queue):
        q = queue.copy()
        for _ in range(len(q)):
            e = q.pop(0)
            if e in q:
                return False
        return True

    def problem(line, n):
        queue = []
        for i in range(n):
            queue.append(line[i])

        position = n
        all_different = different(queue)
        while not all_different:
            queue.append(line[position])
            queue.pop(0)
            all_different = different(queue)
            position += 1
        return str(position)

    datastream = f.read().splitlines()[0]
    print(f'06a - solution for n = 4 is {problem(datastream, 4)}')
    print(f'06b - solution for n = 14 is {problem(datastream, 14)}')
    # time 1h


