# Lendo a quantidade de horas, minutos e segundos do usuário
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

# Convertendo tudo para segundos
# 1 hora = 3600 segundos e 1 minuto = 60 segundos
total_segundos = (horas * 3600) + (minutos * 60) + segundos

# Imprimindo o resultado
print(f"O total em segundos é: {total_segundos} segundos")
