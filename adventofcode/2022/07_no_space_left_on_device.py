def get_structure(data):
    # struc = {} dictionary of (path) --> size
    # path = [] list of filenames
    # sizes = [] list of sizes
    for line in data:
        if line == '$ cd /':
            path = ['/']
            sizes = [0]
            struc = {tuple(path): 0}
        elif line == '$ cd ..':
            # go one way down in path
            subdir_size = sizes.pop()
            path[-1] = path[-1] + ' dir'
            struc[tuple(path)] = subdir_size
            path.pop()
            sizes[-1] += subdir_size
        elif line.startswith('$ cd '):
            # go one way up in pos
            path.append(line[5:])
            sizes.append(0)
        elif line == '$ ls':
            pass
        else:
            # add to struc
            line_list = line.split(' ')
            p = path.copy()
            if line_list[0] == 'dir':
                # directory to add
                p.append(line_list[1] + ' dir')
                struc[tuple(p)] = 0
            else:
                # file to add
                p.append(line_list[1])
                file_size = int(line_list[0])
                struc[tuple(p)] = file_size
                sizes[-1] += file_size
    # add directories we ended in
    for i in range(len(path)-1):
        subdir_size = sizes.pop()
        path[-1] = path[-1] + ' dir'
        struc[tuple(path)] = subdir_size
        path.pop()
        sizes[-1] += subdir_size
    struc[tuple(['/'])] = sizes[0]

    return struc


with open('resources/07.txt') as f:
    lines = f.read().splitlines()
    structure = get_structure(lines)

    sum1 = 0
    max2 = structure[tuple(['/'])]
    min_deleted = max2
    for key, value in structure.items():
        if value <= 100000 and key[-1].endswith(' dir'):
            sum1 += value
        if (max2 - value < 40000000) and (value < min_deleted) and key[-1].endswith(' dir'):
            min_deleted = value

    print(f'07a - sum of small directories is {str(sum1)}')
    print(f'07b - min size directory to delete has size {str(min_deleted)}')
    # time 2h







