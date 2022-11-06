# 3) Ler valor inteiro em segundos e informar em horas:minutos:segundos:

import os
import time

while True:
    os.system("cls")
    
    n = int(input("Digite o valor em segundos: "))
    horas = n // 60**2
    n = n - horas * 60**2
    minutos = n // 60
    n = n - minutos*60
    segundos = n
    print(f'\n{horas}:{minutos}:{segundos}')
    
    time.sleep(10)
