def calcular_menor_preco_por_kg(num_supermercados, precos_quantidades):
    menor_preco_por_kg = float('inf')

    for preco, quantidade in precos_quantidades:
        preco_por_kg = (preco / quantidade) * 1000
        if preco_por_kg < menor_preco_por_kg:
            menor_preco_por_kg = preco_por_kg

    return round(menor_preco_por_kg, 2)

def main():
    num_supermercados = int(input())
    precos_quantidades = []

    for _ in range(num_supermercados):
        dados = input().split()
        preco, quantidade = float(dados[0]), int(dados[1])
        precos_quantidades.append((preco, quantidade))

    menor_preco = calcular_menor_preco_por_kg(num_supermercados, precos_quantidades)
    print(f"{menor_preco:.2f}")

if __name__ == "__main__":
    main()
