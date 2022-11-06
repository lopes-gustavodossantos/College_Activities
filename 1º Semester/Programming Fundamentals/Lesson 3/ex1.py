# 1) Vendedor, Salário Fixo + Comissão de 15% ao mês:

import os
import time

while True:
    os.system("cls")
    
    nome = input("Informe o nome do vendedor: ").title()
    salario_fixo = float(input(f'Informe o Salário Fixo de {nome}: ').replace(",", "."))
    vendas = float(input(f'Informe o valor total em vendas feitas por {nome} no mês: ').replace(',', '.'))
    
    if vendas < 1000:               
        comissao = (vendas*0.15) + salario_fixo
        print(f'\nVendedor: {nome} \nSalário Fixo: R${salario_fixo} \nValor total em vendas: R${vendas:.2f} \nTotal = RS${comissao:.2f}')
        
    elif vendas < 2000:
        comissao = (vendas*0.20) + salario_fixo
        print(f'\nVendedor: {nome} \nSalário Fixo: R${salario_fixo} \nValor total em vendas: R${vendas:.2f} \nTotal = RS${comissao:.2f}')
        
    else:
        comissao = (vendas*0.25) + salario_fixo
        print(f'\nVendedor: {nome} \nSalário Fixo: R${salario_fixo} \nValor total em vendas: R${vendas:.2f} \nTotal = RS${comissao:.2f}')
        
    time.sleep(10)
