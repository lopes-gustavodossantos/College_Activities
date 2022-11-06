# 22) Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utiliza o operador módulo (resto da divisão).

import os

os.system("cls")

numero = int(input("Digite um número inteiro par verificar se o mesmo é par ou ímpar: "))

if numero == 0:
    print("\nNeutro")
elif numero % 2 == 0:
    print("\nPar")
else:
    print("\nÍmpar")
