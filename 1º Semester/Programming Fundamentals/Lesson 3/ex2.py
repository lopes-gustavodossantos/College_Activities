# 2) A, B, C e D, mostrar a diferença do produto de A e B, e C e D:

import os
import time
    
while True:    
    os.system("cls")
    
    a = int(input("Informe um valor inteiro: "))
    b = int(input("Informe um valor inteiro para multiplicar pelo anterior: "))
    print(f'{a} x {b} = {a * b}\n ')
    
    c = int(input("Informe um valor inteiro: "))
    d = int(input("Informe um valor inteiro para multiplicar pelo anterior: "))
    print(f'{c} x {d} = {c * d}')
    print(f' \nDIFERENÇA = {a * b - c * d}')
    
    time.sleep(10)
