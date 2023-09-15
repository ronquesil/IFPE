#Faça um programa que solicita a idade do carro do usuário e, em seguida, indica:
#Que o carro é novo, se o carro tiver menos de 3 anos
#Que o carro é velho, em caso contrário

idade - int(input())
if idade <= 3:
    print ("Carro novo")
if idade > 3:
    print ("Carro velho")