# Receber o preço do produto e o código de pagamento
preco = float(input())
codigo = int(input())

# Inicializar as variáveis para o desconto e número de prestações
desconto = 0
n_prestacoes = 0

# Calcular o desconto e o número de prestações de acordo com o código
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

# Calcular o preço com desconto e o valor de cada prestação
preco_com_desconto = preco * (1 - desconto / 100)
valor_prestacao = preco_com_desconto / n_prestacoes

# Exibir o resultado
print(f"{n_prestacoes}x de R$ {valor_prestacao:.2f}")
