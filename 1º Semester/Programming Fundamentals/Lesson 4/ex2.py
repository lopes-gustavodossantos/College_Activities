# 2) Ler 3 valores e verificar se ambos podem formar um Triângulo, caso positivo verificar se é um Triângulo Retângulo:

import os
import time

while True:
    os.system("cls")
    
    a = int(input("(1/3) Digite o Valor 1: ")) 
    b = int(input("(2/3) Digite o Valor 2: "))
    c = int(input("(3/3) Digite o Valor 3: "))
    
    if a < b + c and b < a + c and c < a + b: 
        if a == b == c:                 
            print("\nVálido - Equilátero")
        elif a != b != c != a:           
            print("\nVálido - Escaleno")
            if a**2 + b**2 == c**2:     
                print("Retângulo: Sim")
            else:
                print("Retângulo: Não")
        elif a == b or a == c or b == c: 
            print("\nVálido - Isósceles")
            if a**2 + b**2 == c**2:      
                print("Retângulo: Sim")
            else:
                print("Retângulo: Não")
    else:
        print("\nInválido")
        
    time.sleep(5)
