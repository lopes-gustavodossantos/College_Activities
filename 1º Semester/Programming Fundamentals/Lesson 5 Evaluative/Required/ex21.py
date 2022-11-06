# 21) Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#     As notas diponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#       a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#       b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

import os

os.system("cls")

valor = int(input("Valor Mímimo: R$ 10,00 \nValor Máximo: R$ 600,00 \nDigite o valor desejado: "))

if 10 <= valor <= 600:
    cem = valor // 100
    valor = valor - (cem * 100)
    cinquenta = valor //50
    valor = valor - (cinquenta * 50)
    dez = valor // 10
    valor = valor - (dez * 10)
    cinco = valor // 5
    valor = valor - (cinco * 5)
    um = valor
    
    if cem == 1:
        notas100 = "nota"
    else:
        notas100 = "notas"
    if cinquenta == 1:
        notas50 = "nota"
    else:
        notas50 = "notas"
    if dez == 1:
        notas10 = "nota"
    else:
        notas10 = "notas"
    if cinco == 1:
        notas5 = "nota"
    else:
        notas5 = "notas"
    if um == 1:
        notas1 = "nota"
    else:
        notas1 = "notas"
        
    print(f'\n{cem} {notas100} de R$ 100 \n{cinquenta} {notas50} de R$ 50 \n{dez} {notas10} de R$ 10 \n{cinco} {notas5} de R$ 5 \n{um} {notas1} de R$ 1')
    
else:
    print("\nValor exigido fora do limite aceito pelo Sistema!")
