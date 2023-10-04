# Receber os ângulos do triângulo
angulo1 = float(input())
angulo2 = float(input())
angulo3 = float(input())

# Verificar o tipo de triângulo com base nos ângulos
if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Retângulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("Obtusângulo")
else:
    print("Acutângulo")