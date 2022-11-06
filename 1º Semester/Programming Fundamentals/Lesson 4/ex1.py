# 1) Ler números de 1 a 12 e apresentar o mês correspondente como resposta:

import os
import time

while True:
    os.system("cls")
    
    numero = int(input("Informe um valor (inteiro) de 1 a 12: "))
    meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    print(f'\nO número {numero} corresponde ao mês de {meses[numero]}')
    
    time.sleep(3) 
