# 2) Há muito, muito tempo atrás

import os

os.system("cls")

imt = int(input("Informe um número: "))
sub = 0
i = 0

while i < imt:
    ano = int(input())
    sub = ano - 2015
   
    if sub < 0:
        print(f'{-sub} D.C.')
    else:
        print(f'{sub + 1} A.C.')
    i += 1
