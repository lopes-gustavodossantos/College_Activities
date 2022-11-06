# 1) Troca em Vetor I

import os

os.system("cls")

n=[]

for i in range(20):
    x = int(input("Informe 20 valores inteiros: "))
    n.append(x)
    
a = n[::-1]

for j in range(20):
    print(f'N[{j + 1}] = {a[j]}')
