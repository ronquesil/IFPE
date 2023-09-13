# Constantes para o custo por dia e por km
CUSTO_POR_DIA = 100.00
CUSTO_POR_KM = 0.50

# Lendo a quantidade de dias e km percorridos
dias_alugado = int(input("Quantidade de dias pelos quais o carro foi alugado: "))
km_percorridos = float(input("Quantidade de km percorridos: "))

# Calculando o custo total
custo_total = (dias_alugado * CUSTO_POR_DIA) + (km_percorridos * CUSTO_POR_KM)

# Imprimindo o custo total
print(f"R$ {custo_total:.2f}")
