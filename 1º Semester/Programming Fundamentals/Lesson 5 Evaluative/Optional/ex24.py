# 24) Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#       a. par ou ímpar;
#       b. positivo ou negativo;
#       c. inteiro ou decimal.

import os

os.system("cls")

valor1 = float(input("(1/2) Informe um valor: ").replace(",", "."))
valor2 = float(input("(2/2) Informe um valor: ").replace(",", "."))
operacao = int(input(f'\nValor 1: {valor1} \nValor 2: {valor2} \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \nQual das operações acima deseja realizar com os valores? '))

if operacao == 1:
    total = valor1 + valor2
    op = "+"
elif operacao == 2:
    total = valor1 - valor2
    op = "-"
elif  operacao == 3:
    total = valor1 * valor2
    op = "x"
elif operacao == 4:
    if valor2 == 0:
        total = 0
    else:
        total = valor1 / valor2
    op = '/'
else:
    print("\nOperação não reconhecida pelo Sistema.")

if total == 0:
    par_impar = "Neutro"
elif total % 2 == 0:
    par_impar = "Par"
else:
    par_impar = "Ímpar"

if total > 0:
    posi_nega = "Positivo"
elif total < 0:
    posi_nega = "Negativo"
else:
    posi_nega = "Neutro"

if total % 1 == 0:
    int_deci = "Inteiro"
else:
    int_deci = "Decimal"

print(f'\n{valor1} {op} {valor2} = {total} \nPar ou Ímpar: {par_impar} \nPositivo ou Negativo: {posi_nega} \nInteiro ou Decimal: {int_deci}')
