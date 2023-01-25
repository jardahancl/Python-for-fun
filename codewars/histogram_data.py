def histogram(values, bin_width):
    if len(values) == 0:
        return []
    m = max(values)
    result = []
    for i in range(m // bin_width + 1):
        count = 0
        for l in range(bin_width):
            count += values.count(i*bin_width + l)
        result.append(count)
    return result

print(histogram([1, 1, 0, 1, 3, 2, 6], 1))
print(histogram([1, 1, 0, 1, 3, 2, 6], 2))
print(histogram([], 1))