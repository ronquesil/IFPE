precos = {
    1: {'nome': 'Maçã', 'preco_ate_5kg': 7.00, 'preco_acima_5kg': 5.80},
    2: {'nome': 'Pêra', 'preco_ate_5kg': 11.80, 'preco_acima_5kg': 8.50},
    3: {'nome': 'Laranja', 'preco_ate_5kg': 2.25, 'preco_acima_5kg': 1.70},
    4: {'nome': 'Banana', 'preco_ate_5kg': 5.50, 'preco_acima_5kg': 4.00},
    5: {'nome': 'Tomate', 'preco_ate_5kg': 6.90, 'preco_acima_5kg': 5.50},
    6: {'nome': 'Cebola', 'preco_ate_5kg': 4.50, 'preco_acima_5kg': 2.40},
}

codigo = int(input())
quantidade = float(input())

preco_total = 0

if codigo in precos:
    if quantidade <= 5:
        preco_total = quantidade * precos[codigo]['preco_ate_5kg']
    else:
        preco_total = quantidade * precos[codigo]['preco_acima_5kg']
    print(f"R$ {preco_total:.2f}")
else:
    print("Código de fruta inválido.")
