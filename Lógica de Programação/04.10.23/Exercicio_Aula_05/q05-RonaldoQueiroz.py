preco = float(input())
codigo = int(input())

desconto = 0
n_prestacoes = 0

if codigo == 1:
    desconto = 30
    n_prestacoes = 1
elif codigo == 2:
    desconto = 20
    n_prestacoes = 2
elif codigo == 3:
    desconto = 10
    n_prestacoes = 3
elif codigo == 4:
    desconto = 0
    n_prestacoes = 4
else:
    print("ERRO")
    exit()

preco_com_desconto = preco * (1 - desconto / 100)
valor_prestacao = preco_com_desconto / n_prestacoes

# Exibir o resultado
print(f"{n_prestacoes}x de R$ {valor_prestacao:.2f}")
