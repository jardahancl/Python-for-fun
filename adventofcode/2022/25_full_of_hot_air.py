with open('resources/25.txt') as file:
    snafus = file.read().splitlines()
print(snafus)


def digit_to_integer(snf):
    if snf.isnumeric():
        return int(snf)
    elif snf == '-':
        return -1
    elif snf == '=':
        return -2


def to_integer(snf):
    result = 0
    base = 1
    for pos in range(len(snf) - 1, -1, -1):
        result += digit_to_integer(snf[pos]) * base
        base *= 5
    return result


def digit_to_snafu(n):
    if n < 3:
        return str(n), -n
    elif n == 3:
        return '=', 2
    elif n == 4:
        return '-', 1


def to_snafu(number):
    result = ''
    while number >= 1:
        div, rest = digit_to_snafu(number % 5)
        result += div
        number = (number + rest) // 5
    return result[::-1]


sol_1 = 0
for snafu in snafus:
    sol_1 += to_integer(snafu)
    print(to_integer(snafu))


print(f"25a - I supply number {to_snafu(sol_1)} to Bob's console.")
# time 1h


