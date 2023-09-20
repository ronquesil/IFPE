num1 = int(input())
num2 = int(input())
opcao = int(input())

if opcao == 1:
    resultado = num1 ** num2
elif opcao == 2:
    resultado = num1**2 + num2**2
elif opcao == 3:
    resultado = (num1 ** 0.5) + (num2 ** 0.5)
else:
    resultado = "ERRO"

if resultado != "ERRO":
    print(f"{resultado:.1f}")
else:
    print(resultado)