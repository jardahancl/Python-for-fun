import math


def mobius(n):
    result = -1
    i = 2
    while i <= math.floor(math.sqrt(n)):
        if (n % i == 0):
                if n % (i*i) == 0:
                    return 0
                result = - result
                n = n / i
        i += 1
    return result




print(mobius(10))
print(mobius(9))
print(mobius(8))
print(mobius(7))
print(mobius(5))
print(mobius(100000000001))