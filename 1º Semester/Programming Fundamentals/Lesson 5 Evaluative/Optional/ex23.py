# 23) Faça um Proagram que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

import os

os.system("cls")

numero = float(input("Informe um número: ").replace(",", "."))

if numero % 1 == 0:
    print(f'\nO número {numero:.0f} é inteiro!')
else:
    print(f'\nO número {numero} é decimal!')
