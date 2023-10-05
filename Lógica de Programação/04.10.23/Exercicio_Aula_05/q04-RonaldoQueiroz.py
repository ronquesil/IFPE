angulo1 = float(input())
angulo2 = float(input())
angulo3 = float(input())

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Retângulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("Obtusângulo")
else:
    print("Acutângulo")