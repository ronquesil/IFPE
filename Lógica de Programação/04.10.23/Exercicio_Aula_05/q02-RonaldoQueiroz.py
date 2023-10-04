# Receber o custo de fábrica do carro
custo_fabrica = float(input())

# Inicializar as variáveis para as porcentagens
percent_distribuidor = 0
percent_impostos = 0

# Determinar as porcentagens com base no custo de fábrica
if custo_fabrica < 35000:
    percent_distribuidor = 5
    percent_impostos = 0
elif 35000 <= custo_fabrica <= 70000:
    percent_distribuidor = 10
    percent_impostos = 15
else:
    percent_distribuidor = 15
    percent_impostos = 20

# Calcular o preço ao consumidor
preco_consumidor = custo_fabrica + (custo_fabrica * percent_distribuidor / 100) + (custo_fabrica * percent_impostos / 100)

# Mostrar o preço ao consumidor
print(f"R$ {preco_consumidor:.2f}")