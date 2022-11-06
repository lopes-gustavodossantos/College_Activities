# 13) Faça um Programa que leia um número e exiba o dia correspondente da semana.
#     (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

import os

os.system("cls")

numero = int(input("Informe um número (inteiro) de 1 a 7: "))
dias = ["", "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

if 1 <= numero <=7:
    print(f'\nO número {numero} corresponde à {dias[numero]}')
else:
    print("\nValor Inválido")
