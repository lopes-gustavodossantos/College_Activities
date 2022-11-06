# 5) Cálculo de IMC:

import os
import time

while True:
    os.system("cls")
    
    peso = float(input("Informe seu peso: ").replace(',', '.'))
    altura = float(input("Informe sua altura(em metros): ").replace(',', '.'))
    imc = peso / (altura * altura)
    
    if imc <18.5:                                         
        print(f'\nSeu IMC é {imc:.1f}. Peso abaixo da média!') 
        
    elif (imc < 25) and (imc >= 18.5):                     
        print(f'\nSeu IMC é {imc:.1f}. Peso normal!')
        
    elif (imc < 30) and (imc >= 25):                      
        print(f'\nSeu IMC é {imc:.1f}. Acima do peso ideal!')
        
    elif imc >=30:                                         
        print(f'\nSeu IMC é {imc:.1f}. Início de obesidade.')
        
    time.sleep(5)
