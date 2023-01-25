def sum_priorities(letters):
    result = 0
    for l in letters:
        if l.islower():
            result += ord(l) - ord('a') + 1
        else:
            result += ord(l) - ord('A') + 27
    return result


data = open('resources/03.txt').read().splitlines()

divided = list(map(lambda x: [x[:len(x) // 2], x[len(x) // 2:]], data))
intersecting = list(map(lambda x: ''.join(set(x[0]).intersection(x[1])), divided))

group_size = 3
grouped = [data[i * group_size:(i + 1) * group_size] for i in range((len(data) + group_size - 1) // group_size)]
intersecting_3 = list(map(lambda x: ''.join(set(''.join(set(x[0]).intersection(x[1]))).intersection(x[2])), grouped))

print(f'03a - {sum_priorities(intersecting)}')
print(f'03b - {sum_priorities(intersecting_3)}')
# time 45m
