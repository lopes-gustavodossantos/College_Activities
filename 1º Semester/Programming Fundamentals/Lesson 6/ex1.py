# 1) Soma de Ímpares Consecutivos

import os
import time

while True:
    os.system("cls")
    
    testes = int(input("Informe a quantidade de testes: "))
    
    for i in range(0, testes):
        valores = input("Números: ").split()
        x = int(valores[0])
        y = int(valores[1])

        if x % 2 == 0:
            x += 1

        soma = 0
        
        for j in range(0, y):
            soma += x
            x += 2
            
        print(soma)
        
        time.sleep(2)
