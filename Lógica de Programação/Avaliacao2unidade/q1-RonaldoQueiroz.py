def calcular_media_salarios(salarios):
    return sum(salarios) / len(salarios)

def calcular_media_filhos(filhos):
    return sum(filhos) / len(filhos)

def encontrar_maior_salario(salarios):
    return max(salarios)

def calcular_percentual_abaixo_limite(salarios, limite):
    abaixo_limite = sum(1 for salario in salarios if salario < limite)
    return (abaixo_limite / len(salarios)) * 100

def ler_dados():
    n = int(input())
    salarios = []
    filhos = []

    for _ in range(n):
        salario, num_filhos = map(float, input().split())
        salarios.append(salario)
        filhos.append(num_filhos)

    return salarios, filhos

def main():
    salarios, filhos = ler_dados()

    media_salarios = calcular_media_salarios(salarios)
    media_filhos = calcular_media_filhos(filhos)
    maior_salario = encontrar_maior_salario(salarios)
    percentual_abaixo_1212 = calcular_percentual_abaixo_limite(salarios, 1212.00)

    print(f"MÉDIA SALARIAL = R$ {media_salarios:.2f}")
    print(f"MÉDIA FILHOS = {media_filhos:.1f}")
    print(f"MAIOR SALÁRIO = R$ {maior_salario:.2f}")
    print(f"PERCENTUAL = {percentual_abaixo_1212:.2f}%")

if __name__ == "__main__":
    main()
