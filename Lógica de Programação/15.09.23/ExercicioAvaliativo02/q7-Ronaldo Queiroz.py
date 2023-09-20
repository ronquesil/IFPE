salario_minimo = 1212.00  # Altere conforme necessário

salario_atual = float(input())

if salario_atual <= salario_minimo:
    percentual_aumento = 20
else:
    percentual_aumento = 15

salario_reajustado = salario_atual + (salario_atual * percentual_aumento / 100)

print(f"R$ {salario_reajustado:.2f}")