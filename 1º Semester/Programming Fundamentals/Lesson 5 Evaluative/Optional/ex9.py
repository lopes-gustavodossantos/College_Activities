# 9) Faça um Programa que leia três números e mostre-os em orddem decescente.

import os

os.system("cls")

numeros = []
repeticao = 3

for i in range(repeticao):
    valores = float(input("Informe um número: ").replace(",", "."))
    numeros.append(valores)
    
numeros.sort(reverse = True)
print(f'\n{numeros[0]}, {numeros[1]}, {numeros[2]}')
