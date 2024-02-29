def maior_elemento_acima_diagonal(matriz):
    n = len(matriz)
    maior_valor = float('-inf')

    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]

    return maior_valor

def main():
    n = int(input())
    matriz = []

    print()
    for i in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    maior_valor = maior_elemento_acima_diagonal(matriz)
    print(maior_valor)

if __name__ == "__main__":
    main()
