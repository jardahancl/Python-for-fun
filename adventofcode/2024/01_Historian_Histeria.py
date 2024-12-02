list1 = []
list2 = []
# local_sum = 0
for line in open('resources/01.txt').read().splitlines():
    vals = list(line.split(" "))
    print(vals)
    list1.append(int(vals[0]))
    list2.append(int(vals[3]))
list1.sort()
list2.sort()

sums = []
for t, u in zip(list1, list2):
    sums.append(abs(t - u))

multi = []
for x in list1:
    multi.append(x * list2.count(x))


print(f'01a - difference is {sum(sums)}')
print(f'01b - score is {sum(multi)}')
# 20m