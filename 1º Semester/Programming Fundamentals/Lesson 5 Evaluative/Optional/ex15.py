# 15) Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#     Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceito;
#     Triângulo Equilátero: trêa lados iguais;
#     Triângulo Isósceles: quaisquer dois lados iguais;
#     Triângulo Escaleno: três lados diferentes;

import os

os.system("cls")

a = int(input("(1/3) Digite o Valor 1: "))
b = int(input("(2/3) Digite o Valor 2: "))
c = int(input("(3/3) Digite o Valor 3: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("\nEstes valores podem formar um Triângulo Equilátero!")
    elif a != b != c != a:
        print("\nEstes valores podem formar um Triângulo Escaleno!")
    elif a == b or a== c or b == c:
        print("\nEstes valores podem formar um Triângulo Isósceles")
else:
    print("\nEstes valores não podem formar um triângulo")
