# Ler os valores de a e b
a = int(input())
b = int(input())

# Inicializar resultado como 1 (qualquer número elevado a 0 é 1)
resultado = 1

# Usar um loop para multiplicar a por ele mesmo b vezes
for _ in range(b):
    resultado *= a

# Exibir o resultado
print(resultado)