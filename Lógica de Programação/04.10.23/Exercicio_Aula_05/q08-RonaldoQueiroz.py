# Receber o número para o qual se deseja calcular a tabuada
num = int(input())

# Loop para calcular e exibir a tabuada
for i in range(1, 11):
    resultado = num * i
    print(f"{num}x{i} = {resultado}")