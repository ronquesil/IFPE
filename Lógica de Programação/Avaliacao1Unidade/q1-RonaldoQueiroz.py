def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

soma_primos = 0

while True:
    numero = int(input())
    if numero == 0:
        break
    if is_prime(numero):
        soma_primos += numero

print(soma_primos)
