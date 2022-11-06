# 1) Faça um Programa que peça dois números e leia o maior deles.

import os

os.system("cls")

numero1 = float(input("(1/2) Informe um número: ").replace(",", "."))
numero2 = float(input("(2/2) Informe um número: ").replace(",", "."))

if numero1 > numero2:
    print(numero1)
else:
    print(numero2)
