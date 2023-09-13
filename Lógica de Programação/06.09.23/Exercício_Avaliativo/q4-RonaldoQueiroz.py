# Solicitando o preço da mercadoria e o percentual de desconto do usuário
preco_mercadoria = float(input("Insira o preço da mercadoria : "))
percentual_desconto = float(input("Insira o percentual de desconto : "))

# Calculando o valor do desconto
valor_desconto = (preco_mercadoria * percentual_desconto) / 100

# Calculando o preço final a pagar
preco_a_pagar = preco_mercadoria - valor_desconto

# Imprimindo o valor do desconto e o preço a pagar
print(f"O valor do desconto é de R$ {valor_desconto:.2f}")
print(f"O valor a pargar é de R$ {preco_a_pagar:.2f}")