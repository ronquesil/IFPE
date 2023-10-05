def calcula_credito(saldo_medio):
    if saldo_medio > 400:
        percentual_credito = 0.30
    elif 300 <= saldo_medio <= 400:
        percentual_credito = 0.25
    elif 200 <= saldo_medio < 300:
        percentual_credito = 0.20
    else:
        percentual_credito = 0.10

    valor_credito = saldo_medio * percentual_credito
    return valor_credito

saldo_medio = float(input("Digite o saldo médio do cliente: ").replace(',', '.'))

valor_credito = calcula_credito(saldo_medio)

print(f"O valor do crédito concedido ao cliente é: R$ {valor_credito:.2f}")
