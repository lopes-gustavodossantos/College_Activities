# 5) Faça um programa para leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#    a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    b. A mensagem "Reprovado", se a média for menor que sete;
#    c. A mensagem "Aprovado com Distinção", se a média for igual a dez.

import os

os.system("cls")

nota1 = float(input("Informe a primeira nota: ").replace(",", "."))
nota2 = float(input("Informe a segunda nota: ").replace(",", "."))
media = (nota1 + nota2) / 2

if 7 <= media < 10:
    print(f'\nAprovado, sua média é {media:.2f}')
elif media < 7:
    print(f'\nReprovado, sua média é {media:.2f}')
else:
    print(f'\nAprovado com Distinção, sua média é {media:.2f}')
