custo_fabrica = float(input())

percent_distribuidor = 0
percent_impostos = 0

if custo_fabrica < 35000:
    percent_distribuidor = 5
    percent_impostos = 0
elif 35000 <= custo_fabrica <= 70000:
    percent_distribuidor = 10
    percent_impostos = 15
else:
    percent_distribuidor = 15
    percent_impostos = 20

preco_consumidor = custo_fabrica + (custo_fabrica * percent_distribuidor / 100) + (custo_fabrica * percent_impostos / 100)

print(f"R$ {preco_consumidor:.2f}")