def calcular_moedas_do_capitao(A, N):
    X = A // (N + 2)
    moedas_do_capitao = 2 * X
    return moedas_do_capitao

A = int(input())
N = int(input())

moedas_do_capitao = calcular_moedas_do_capitao(A, N)
print(moedas_do_capitao)