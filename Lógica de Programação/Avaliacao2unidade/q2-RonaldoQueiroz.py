resultados = input()

frequencias = [resultados.count(str(i)) for i in range(1, 7)]

for i, freq in enumerate(frequencias):
    print(f"Número {i+1} saiu {freq} vezes.")