def processar_numeros(numeros, codigo):
    if codigo == 0:
        return -1
    elif codigo == 1:
        return [num * 2 for num in numeros]
    elif codigo == 2:
        return numeros[::-1]
    else:
        return "Código inválido"

entrada_numeros = input()
entrada_codigo = int(input())

numeros = [int(num) for num in entrada_numeros.split()]

saida = processar_numeros(numeros, entrada_codigo)
print(saida)
