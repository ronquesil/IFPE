# Recebe uma string de números representando os resultados de 20 lançamentos de um dado
resultados = input("Insira os resultados dos lançamentos do dado: ")

# Conta a frequência de cada número
frequencias = [resultados.count(str(i)) for i in range(1, 7)]

# Imprime a frequência de cada número
for i, freq in enumerate(frequencias):
    print(f"Número {i+1} saiu {freq} vezes.")