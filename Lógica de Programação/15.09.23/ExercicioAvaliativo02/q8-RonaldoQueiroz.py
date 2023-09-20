nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2) / 2

if 0.0 <= media < 3.0:
    mensagem = "Reprovado"
elif 3.0 <= media < 7.0:
    mensagem = "Exame"
elif 7.0 <= media <= 10.0:
    mensagem = "Aprovado"

print(f"{media:.1f} - {mensagem}")