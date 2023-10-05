num_limite = int(input())

numeros_impares = []

for i in range(1, num_limite + 1):
    if i % 2 != 0:
        numeros_impares.append(str(i))

saida = ' '.join(numeros_impares)

print(saida)