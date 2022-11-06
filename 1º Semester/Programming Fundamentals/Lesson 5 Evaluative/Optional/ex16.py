# 16) Faça um programa que calcule as raizes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#       a. Se o usuário informar o valor A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#       b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#       c. Se o delta calculado for igual a zero a equação possui apenas uma raizes real; informe-a ao usuário.
#       d. Se o delta for positivo, a equação possui duas raizes reais; informe-as ao usuário;

import math
import os

os.system("cls")

a = float(input("ax2 + bx + c \nBaseado na fórmula acima, informe os valores para, \na: "))

if a == 0:
    print("\nDevido à 'a' ser igual a 0, a equação não é de segundo grau.")
else:
    b = float(input("b: "))
    c = float(input("c: "))
    delta = ((b**2) - (4 * a * c))
    
    if delta < 0:
        print("\nDevido ao Delta ser negativo, menor que 0, a equação não possui raízes reais")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f'\nDevido ao Delta ser igual a 0, a equação possui apenas uma raiz real. \nRaiz: {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'\nDevido ao Delta ser positivo, maior que 0, a equação possui duas raízes reais. \nRaiz 1: {raiz1:.2f} \nRaiz 2: {raiz2:.2f}')
