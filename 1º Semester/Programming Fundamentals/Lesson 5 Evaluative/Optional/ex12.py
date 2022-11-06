# 12) Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do Imposto de Renda,
#     que depende do salário bruto(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
#     (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua
#     hora e a quantidade de horas trabalhadas no mês.
#       a. Desconto de IR:
#       b. Salário Bruto até 900 (inclusive) - isento
#       c. Salário Bruto até 2500 (inclusive) - desconto de 5%
#       d. Salário Bruto até 2500 (inclusive) - desconto de 10%
#       e. Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
#           i. Salário Bruto: (5*220) : R$ 1100,00
#          ii. (-) IR (5%) : R$ 55,00
#         iii. (-) INSS (10%) : R$ 110,00
#          iv. FGTS (11%) : R$ 121,00
#           v. Total de descontos : R$ 165,00
#          vi. Salário Líquido : R$ 935,00

import os

os.system("cls")

valor_hora = float(input("Informe quanto você recebe por hora: R$ ").replace(",", "."))
horas_mes = int(input("Informe quantas horas você trabalha por mês: "))

salario_bruto = valor_hora * horas_mes
imposto = salario_bruto * 0.05
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

print(f'\nSalário Bruto: R$ {salario_bruto:.2f} \n(-) Imposto de Renda (5%): R$ {imposto:.2f} \n(-) INSS (10%): R$ {inss:.2f} \nFGTS (11%): {fgts:.2f} \nTotal de descontos: R$ {imposto + inss:.2f} \nSalário Líquido: {salario_bruto - (imposto + inss):.2f}') 
