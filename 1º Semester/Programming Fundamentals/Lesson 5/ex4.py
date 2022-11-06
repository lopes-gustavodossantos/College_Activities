# 4) Ler um número inteiro e mostra-lo invertido:

import os
import time

while True:
    os.system("cls")
    
    numero = int(input("Digite um valor inteiro: "))
    numero = str(numero)
    print(numero[::-1])
    
    time.sleep(5)
