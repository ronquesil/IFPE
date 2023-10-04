# Receber o número para calcular o fatorial
num = int(input())

# Inicializar a variável para o fatorial
fatorial = 1

# Loop para calcular o fatorial
for i in range(1, num + 1):
    fatorial *= i

# Exibir o fatorial
print(fatorial)