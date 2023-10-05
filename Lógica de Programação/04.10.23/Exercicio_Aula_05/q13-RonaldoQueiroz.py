# Ler os valores de n e m
n = int(input())
m = int(input())

# Loop externo para as linhas
for i in range(n):
    # Loop interno para as colunas
    for j in range(m):
        print("#", end="")
    # Quebra de linha após cada linha completa de cerquilhas
    print()