# 2) Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

import os
import time

while True:
    os.system("cls")
    
    valor = float(input("Informe o valor: ").replace(",","."))
    
    if valor > 0:
        print(f'\nO número {valor} é positivo!')
    elif valor < 0:
        print(f'\nO número {valor} é negativo!')
    else:
        print("\nO número 0 é neutro!")
        
    time.sleep(5)
