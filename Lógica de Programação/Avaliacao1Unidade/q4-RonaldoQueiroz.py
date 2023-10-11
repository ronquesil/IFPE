from collections import Counter

def factorize(n):
    factors = Counter()
    i = 2
    while i * i <= n:
        while n % i:
            i += 1
        while n % i == 0:
            n //= i
            factors[i] += 1
    if n > 1:
        factors[n] += 1
    return factors

def count_divisors(n):
    factors = factorize(n)
    divisors = 1
    for exponent in factors.values():
        divisors *= (exponent + 1)
    return divisors

N = int(input("Digite o número N: "))
print(count_divisors(N))
