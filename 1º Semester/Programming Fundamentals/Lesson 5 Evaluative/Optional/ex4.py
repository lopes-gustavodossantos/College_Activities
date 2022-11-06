# 4) Faça um programa que verifique se uma letra digitada é vogal ou consoante.

import os

os.system("cls")

vogais = ["A", "E", "I", "O", "U"]
letra = str(input("Digite uma letra de sua escolha: ").upper())

if letra in vogais:
    print(f'\nA letra "{letra}" é vogal!')
else:
    print(f'\nA letra "{letra}" é consoante!')
