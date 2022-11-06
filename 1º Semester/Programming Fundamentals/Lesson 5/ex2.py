# 2) Ler um valor N, este N será o tamanho de um vetor x[N]:

import os
import time

while True:
    os.system("cls")
    
    tamanho = int(input("Informe um valor inteiro para representar o tamanho do vetor: "))
    vetor = []

    for i in range(tamanho):
        vetor_valores = int(input("Informe os valores inteiros: "))
        vetor.append(vetor_valores)

    print(f'\n{tamanho} \n{vetor} \nMenor valor: {min(vetor)}\nPosição: {vetor.index(min(vetor))}')
    
    time.sleep(10)
