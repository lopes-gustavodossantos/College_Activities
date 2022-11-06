# 3) MacPRONALTS

import os
import time

while True:
    os.system("cls")
    
    pedidos = int(input("Informe a quantidade de produtos comprados: "))
    total = 0
    numeros = []

    for i in range(pedidos):
        codigo, quantidade = input().split(' ')
        codigo = int(codigo)
        quantidade = int(quantidade)

        if codigo == 1001:
            total = quantidade * 1.50
        elif codigo == 1002:
            total = quantidade * 2.50
        elif codigo == 1003:
            total = quantidade * 3.50
        elif codigo == 1004:
            total = quantidade * 4.50
        elif codigo == 1005:
            total = quantidade * 5.50
        numeros.append(total)

    for i in range(len(numeros)):
        numeros[i] = float(numeros[i])
        
    print(f'Total: {sum(numeros):.2f}')
    
    time.sleep(5)
