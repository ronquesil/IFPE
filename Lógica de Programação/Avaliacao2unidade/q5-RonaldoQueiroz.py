def soma_impares_entre(num1, num2):
    return sum(num for num in range(min(num1, num2), max(num1, num2) + 1) if num % 2 != 0)

n1 = int(input())
n2 = int(input())

resultado = soma_impares_entre(n1, n2)
print(f"{resultado}")
