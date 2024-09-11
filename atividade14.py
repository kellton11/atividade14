# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
n1 = float(input("digite 1º nota:"))
n2 = float(input("digite sua 2º nota:"))
n3 = float(input("digite sua 3º nota:"))

média = (n1+n2+n3)/3

if média >=7:
    print("aprovado")
elif média <5:
    print("reprovado")
else:
    print("reprovado")