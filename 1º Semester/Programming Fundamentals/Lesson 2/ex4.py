# 4) Média Aritmética:

import os
import time

while True:
    os.system("cls")
    g1 = float(input("Informe sua nota da G1: ").replace(',', '.')) 
    g2 = float(input("Informe sua nota da G2: ").replace(',', '.'))
    media = float((g1 + g2) / 2)
    
    if media >= 7:                                              
        print(f'\nVocê está acima da média! Sua média é {media:.1f}.')
    else:                                                 
        print(f'\nVocê está abaixo da média! Sua média é {media:.1f}.')
        
    time.sleep(5)
