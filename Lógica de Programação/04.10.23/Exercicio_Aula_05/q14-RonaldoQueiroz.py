while True:
    # Ler m e n
    m, n = map(int, input().split())
    
    if m >= n:
        break
    
    soma = sum(range(m, n + 1))
    
    print(soma, end=" ")