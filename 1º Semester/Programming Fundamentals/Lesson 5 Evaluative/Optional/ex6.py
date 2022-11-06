# 6) Faça um Programa que leia três números e mostre o maior deles.

import os

os.system("cls")

lista_numeros = []
repeticao = 3

for i in range(repeticao):
    numeros = float(input("Informe um número: ").replace(",", "."))
    lista_numeros.append(numeros)
    
lista_numeros.sort(reverse = True)
print(lista_numeros[0])
