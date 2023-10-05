soma_notas = 0
contagem_notas = 0

while True:
    nota = float(input())
    if nota < 0:
        break
    soma_notas += nota
    contagem_notas += 1

if contagem_notas > 0:
    media = soma_notas / contagem_notas
    print(media)
else:
    print("Nenhuma nota válida inserida.")
