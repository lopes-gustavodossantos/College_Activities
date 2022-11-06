# 17) Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

import os

os.system("cls")

ano = int(input("Informe o ano em questão: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\n{ano} é um ano bissexto!')
else:
    print(f'\n{ano} não é um ano bissexto!')
