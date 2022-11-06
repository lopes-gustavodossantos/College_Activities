# 27)                 Até 5 Kg      Acima de 5 kg
#     Morango   R$ 2,50 por Kg     R$ 2,20 por Kg
#     Maçã      R$ 1,80 por Kg     R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

import os

os.system("cls")

morangos = float(input("Informe a quantidade em Kg de Morangos: ").replace(",", "."))
macas = float(input("Informe a quantidade em Kg de Maçãs: ").replace(",", "."))
morangos1 = morangos * 2.50
morangos2 = morangos * 2.20
macas1 = macas * 1.80
macas2 = macas * 1.50

if morangos > 5:
    total_morangos = morangos2
else:
    total_morangos = morangos1
    
if macas > 5:
    total_macas = macas2
else:
    total_macas = macas1

total = total_morangos + total_macas

if total > 25 or (morangos + macas) > 8:
    print(f'\nQuantidade de Morangos (Kg): {morangos} \nQuantidade de Maçãs (Kg): {macas} \nTotal: {total} \nTotal com 10% de desconto: {total - (total * 0.10)}')
else:
    print(f'\nQuantidade de Morangos (Kg): {morangos} \nQuantidade de Maçãs (Kg): {macas} \nTotal: {total}')
