# 10) Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

import os

os.system("cls")

turno = str(input("Turnos: \nM - Matutino \nV - Vespertino \nN - Noturno \nEm qual destes tunos você Estuda? \nInforme digitando a letra correspondente: ").upper())

if turno == "M":
    print("\nBom Dia!")
elif turno == "V":
    print("\nBoa Tarde!")
elif turno == "N":
    print("\nBoa Noite!")
else:
    print("\nValor Inválido!")
