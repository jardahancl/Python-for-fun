import math

def gap(g, m, n):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    for i in range (m, n-g+1):
        if is_prime(i) and is_prime(i+g):
            prime_in_gap = False
            for j in range(i+1, i+g-1):
                if is_prime(j):
                    prime_in_gap = True
            if not prime_in_gap:
                return [i, i+g]
    return None


print(gap(2,100,110))
print(gap(8,300,400))
print(gap(10,300,400))
