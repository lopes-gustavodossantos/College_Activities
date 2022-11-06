# 1) Ler um valor inteiro que será a quantidade de linhas de saída:

import os

os.system("cls")

numero = int(input("Digite um número inteiro maior que 0: "))
x = 1

for i in range(1,numero + 1):
    print(f'{x} {x + 1} {x + 2} PUM')
    x = x + 4
