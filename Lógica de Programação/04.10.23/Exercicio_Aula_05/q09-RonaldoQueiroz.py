# Receber os números iniciais e finais do intervalo
inicio = int(input())
fim = int(input())

# Inicializar uma lista vazia para armazenar os múltiplos de 3
multiplos = []

# Loop para encontrar os múltiplos de 3 no intervalo especificado
for i in range(inicio, fim + 1):
    if i % 3 == 0:
        multiplos.append(str(i))

# Converter a lista de múltiplos de 3 em uma string separada por espaços
saida = ' '.join(multiplos)

# Exibir a saída
print(saida)