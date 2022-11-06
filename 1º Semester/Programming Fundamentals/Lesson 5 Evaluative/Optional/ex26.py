# 26) a. Álcool:
#             i. até 20 litros, desconto de 3% por litro
#            ii. acima de 20 litros, desconto de 5% por litro
#     b. Gasolina:
#             i. até 20 litros, desconto de 4% por litro
#            ii. acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#                calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

import os

os.system("cls")

quantidade = float(input("Informe a quantidade de litros: ").replace(",", "."))
tipo = int(input("1 - Álcool \n2 - Gasolina \nInforme qual o combustível foi utilizado: "))

if tipo == 1 and quantidade <= 20:
    print(f'\nCombustível: Álccol \nValor (Litro): R$ 1,90 \nQuantidade: {quantidade} \nTotal a ser pago: {(quantidade * 1.90) - (quantidade * 0.03):.2f}')
    
elif tipo == 1 and quantidade > 20:
    print(f'\nCombustível: Álcool \nValor (Litro): R$ 1,90 \nQuantidade: {quantidade} \nTotal a ser pago: {(quantidade * 1.90) - (quantidade * 0.05):.2f}')
    
elif tipo == 2 and quantidade <= 20:
    print(f'\nCombustível: Gasolina \nValor (Litro): R$ 2,50 \nQuantidade: {quantidade} \nTotal a ser pago: {(quantidade * 2.50) - (quantidade * 0.04):.2f}')
    
elif tipo == 2 and quantidade > 20:
    print(f'\nCombustível: Gasolina \nValor (Litro): R$ 2,50 \nQuantidade{quantidade} \nTotal a ser pago: {(quantidade * 2.50) - (quantidade * 0.06):.2f}')
    
else:
    print("\nCombustível inválido!")
