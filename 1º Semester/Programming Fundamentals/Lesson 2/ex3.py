# 3) Média de Combustível:

import os
import time

while True:
    os.system("cls")
    
    km = float(input("Informe quantos quilômetros foram percorridos: ").replace(',', '.')) 
    l = float(input("Informe quantos litros foram gastos: ").replace(',', '.'))
    media = km / l                                                                      
    print(f'\nA média de consumo de seu veículo é de {media:.2f} por Litro.')
    
    time.sleep(3)
