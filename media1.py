import os

nomealuno = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

print("\n********** BOLETIM **********")
print("Nome do aluno:", nomealuno)
print(f"Média da etapa: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado ")
elif media >= 5:
    print("Situação: Recuperação ")
else:
    print("Situação: Reprovado ")

print("****************************")
