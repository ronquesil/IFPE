# Loop infinito para continuar lendo os pares de números
while True:
    # Ler m e n
    m, n = map(int, input().split())
    
    # Condição de parada: sair do loop se m >= n
    if m >= n:
        break
    
    # Calcula a soma dos números entre m e n
    soma = sum(range(m, n + 1))
    
    # Imprime a soma
    print(soma, end=" ")