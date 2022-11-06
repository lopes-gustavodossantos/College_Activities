# 20) Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#       a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#       b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#       c. A mensagem "Aprovado com Distinção", se a média for igual a 10.

import os

os.system("cls")

nota1 = float(input("Informe a primeira nota: ").replace(",", "."))
nota2 = float(input("Informe a segunda nota: ").replace(",", "."))
nota3 = float(input("Informe a terceira nota: ").replace(",", "."))
media = (nota1 + nota2 + nota3) /3

if 7 <= media < 10:
    print(f'\nAprovado, sua média é {media:.2f}')
elif media < 7:
    print(f'\nReprovado, sua média é {media:.2f}')
else:
    print(f'\nAprovado com Distinção, sua média é {media:.2f}')
