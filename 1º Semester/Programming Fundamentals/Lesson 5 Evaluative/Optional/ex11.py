# 11) As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
#     a. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#         i. salários até R$ 280,00 (incluindo): aumento de 20%
#        ii. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#       iii. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#        iv. salários de R$ 1500,00 em diante : aumento de 5%
#
#     Após o aumento ser realizado, informe na tela:
#         i. o salário antes do reajuste;
#        ii. o percentual de aumento aplicado;
#       iii. o valor do aumento;
#        iv. o novo salário, após o aumento.

import os

os.system("cls")

salario = float(input("Informe o salário atual do colaborador: ").replace(",", "."))

if salario <= 280:
    reajuste = 0.20
elif 280 < salario <= 700:
    reajuste = 0.15
elif 700 < salario <= 1500:
    reajuste = 0.10
else:
    reajuste = 0.05
    
print(f'\nSalário antes do reajuste: {salario} \nPercentual de aumento aplicado: + {reajuste}% \nValor do aumento: {salario * reajuste:.2f}\nNovo Salário: {(salario * reajuste) + salario:.2f}')
