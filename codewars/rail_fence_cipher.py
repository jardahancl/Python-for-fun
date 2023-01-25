# define permutation
def get_perm(original, n):
    cycle_len = 2 * n - 2
    line_count = len(original) // cycle_len
    perm = []
    map_position = 0

    for j in range(line_count + 1):
        if j * cycle_len < len(original):
            perm.append([map_position, j * cycle_len])
            map_position += 1
    for i in range(1, n - 1):
        for j in range(line_count + 1):
            if (j * cycle_len + i) < len(original):
                perm.append([map_position, j * cycle_len + i])
                map_position += 1
            if ((j + 1) * cycle_len - i) < len(original):
                perm.append([map_position, (j + 1) * cycle_len - i])
                map_position += 1
    for j in range(line_count + 1):
        if j * cycle_len + (n - 1) < len(original):
            perm.append([map_position, j * cycle_len + (n - 1)])
            map_position += 1
    return perm

# from text to rail
def encode_rail_fence_cipher(original, n):
    perm = get_perm(original, n)
    result = []

    for i in range(len(original)):
        pair = []
        for j in range(len(original)):
            if i == perm[j][0]:
                pair = perm[j]
        result.extend(original[pair[1]])

    return ''.join(map(str, result))

# from rail to text
def decode_rail_fence_cipher(original, n):
    def get_perm(original, n):
        cycle_len = 2 * n - 2
        line_count = len(original) // cycle_len
        perm = []
        map_position = 0

        for j in range(line_count + 1):
            if j * cycle_len < len(original):
                perm.append([map_position, j * cycle_len])
                map_position += 1
        for i in range(1, n - 1):
            for j in range(line_count + 1):
                if (j * cycle_len + i) < len(original):
                    perm.append([map_position, j * cycle_len + i])
                    map_position += 1
                if ((j + 1) * cycle_len - i) < len(original):
                    perm.append([map_position, (j + 1) * cycle_len - i])
                    map_position += 1
        for j in range(line_count + 1):
            if j * cycle_len + (n - 1) < len(original):
                perm.append([map_position, j * cycle_len + (n - 1)])
                map_position += 1
        return perm

    perm = get_perm(original, n)
    result = []

    for i in range(len(original)):
        pair = []
        for j in range(len(original)):
            if i == perm[j][1]:
                pair = perm[j]
        result.extend(original[pair[0]])

    return ''.join(map(str, result))

print(encode_rail_fence_cipher("Hello, World!", 3))
# print("Hoo!el,Wrdl l")
print(encode_rail_fence_cipher("Hello, World!", 4))
# print("H !e,Wdloollr")

print(decode_rail_fence_cipher("H !e,Wdloollr", 4))
# print("Hello, World!")
print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))
# print("WEAREDISCOVEREDFLEEATONCE")

