# 3) Ler um valor inteiro, este valor erá a quantidade de vezes que será repetida a palavra "Ho":

import os
import time

while True:
    os.system("cls")
    
    numero = int(input("Digite um valor inteiro: "))
    
    if numero > 0 and numero < 10 ** 8:
        x = "Ho " * numero
        print(f'{x}!')
    else:
        print("Este valor está fora dos limites aceitos!")
        
    time.sleep(3)
