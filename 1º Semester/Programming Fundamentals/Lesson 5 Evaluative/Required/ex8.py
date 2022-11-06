# 8) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

import os

os.system("cls")

produto1 = float(input("(1/3) Informe o valor do produto: ").replace(",", "."))
produto2 = float(input("(2/3) Informe o valor do produto: ").replace(",", "."))
produto3 = float(input("(3/3) Informe o valor do produto: ").replace(",", "."))

if produto1 < produto2 and produto1 < produto3:
    print("\nVocê deverá comprar o primeiro Produto!")
    
elif produto2 < produto1 and produto2 < produto3:
    print("\nVocê deverá comprar o segundo produto!")
    
elif produto3 < produto1 and produto3 < produto2:
    print("\nVocê deverá comprar o terceiro Produto!")
    
else:
    print("\nAmbos os produtos possuem o mesmo preço.")
