# 14) Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#     a. Média de Aproveitamento Conceito
#           i. Entre 9.0 e 10.0   A
#          ii. Entre 7.5 e 9.0    B
#         iii. Entre 6.0 e 7.5    C
#          iv. Entre 4.0 e 6.0    D
#           v. Entre 0 e 4.0      E
#     O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente a mensagem "APROVADO", se o conceito for A, B, ou C ou "Reprovado" se o conceito for D ou E.

import os

os.system("cls")

nota1 = float(input("Informe a primeira nota: ").replace(",", "."))
nota2 = float(input("Informe a segunda nota: ").replace(",", "."))
media = (nota1 + nota2) / 2

if  9 <= media <=10:
    print(f'\nNota 1: {nota1} \nNota 2: {nota2} \nMédia: {media:.2f} \nConceito: A \nSituação: Aprovado')
elif 7.5 <= media < 9:
    print(f'\nNota 1: {nota1} \nNota 2: {nota2} \nMédia: {media:.2f} \nConceito: B \nSituação: Aprovado')
elif 6 <= media < 7.5:
    print(f'\nNota 1; {nota1} \nNota 2: {nota2} \nMédia: {media:.2f} \nConceito: C \nSituação: Aprovado')
elif 4 <= media < 6:
    print(f'\nNota 1: {nota1} \nNota 2: {nota2} \nMédia: {media:.2f} \nConceito: D \nSituação: Reprovado')
elif 0 <= media < 4:
    print(f'\nNota 1: {nota1} \nNota 2: {nota2} \nMédia: {media:.2f} \nConceito: E \nSituação: Reprovado')
else:
    print("\nOs valores das notas são inválidos")
