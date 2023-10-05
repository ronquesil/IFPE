num = int(input())

eh_primo = True

if num <= 1:
    eh_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break

if eh_primo:
    print("Sim")
else:
    print("Não")