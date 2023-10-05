# Receber o número a ser verificado
num = int(input())

# Inicializar a variável para verificar se o número é primo
eh_primo = True

# Verificar se o número é primo
if num <= 1:
    eh_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break

# Exibir o resultado
if eh_primo:
    print("Sim")
else:
    print("Não")