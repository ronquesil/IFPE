def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = 0

while True:
    try:
        num = int(input())
        if num == 0:
            break
        if is_prime(num):
            prime_sum += num
    except ValueError:
        print("Por favor, digite um número inteiro.")

print(prime_sum)
