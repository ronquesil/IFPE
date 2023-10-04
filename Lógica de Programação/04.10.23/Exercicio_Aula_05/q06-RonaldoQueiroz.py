# Receber o número limite
num_limite = int(input())

# Inicializar uma lista vazia para armazenar os números ímpares
numeros_impares = []

# Loop para encontrar os números ímpares de 1 até num_limite
for i in range(1, num_limite + 1):
    if i % 2 != 0:
        numeros_impares.append(str(i))

# Converter a lista de números ímpares em uma string separada por espaços
saida = ' '.join(numeros_impares)

# Exibir a saída
print(saida)