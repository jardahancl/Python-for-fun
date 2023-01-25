def stat(strg):
    def to_out(n):
        return '|'.join([str(n // 3600).zfill(2), str((n % 3600) // 60).zfill(2), str(n % 60).zfill(2)])

    if len(strg) == 0:
        return ''
    data = [d.split('|') for d in strg.split(', ')]
    times = [int(l[2]) + (int(l[1]) * 60) + (int(l[0]) * 3600) for l in data]
    range = max(times) - min(times)
    average = sum(times) // len(times)
    if (len(times) % 2 == 1):
        median = sorted(times)[len(times) // 2]
    else:
        median = (sorted(times)[(len(times)-1) // 2] + sorted(times)[(len(times)+1) // 2]) // 2

    return ' '.join(['Range: ' + to_out(range), 'Average: ' + to_out(average), 'Median: ' + to_out(median)])


print(stat("01.txt|15|59, 1|47|16, 01.txt|17|20, 1|32|34, 2|17|17"))
# "Range: 01.txt|01.txt|18 Average: 01.txt|38|05 Median: 01.txt|32|34"