#Faça um programa que recebe duas notas de um aluno, calcule e mostre a média aritmética e uma das mensagens a seguir:
#Se media >= 0.0 e media < 2.0, o aluno foi reprovado
#Se media >= 2.0 e media < 7.0, o aluno foi prova final
#Se media >= 7.0 e media <= 10.0, o aluno foi aprovado
#Aos alunos que ficaram para prova final, calcule e mostre a nota que deverão tirar para serem aprovados, considerando que a média final exigida é 6.0

n1 = float(input())
n2 = float(input())

media = (n1+n2)/2

#if media >= and media <= 2:
if 0 <= media < 2:
    print("Reprovado")
if 2 <= media < 7:
    print("Prova final")
    pf = 12 - media
    print(f"Prova final = {pf:.1f}")
if 7 >= media <= 10:
    print("Aprovado")