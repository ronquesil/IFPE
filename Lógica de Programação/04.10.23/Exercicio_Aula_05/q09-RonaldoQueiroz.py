inicio = int(input())
fim = int(input())

multiplos = []

for i in range(inicio, fim + 1):
    if i % 3 == 0:
        multiplos.append(str(i))

saida = ' '.join(multiplos)

print(saida)