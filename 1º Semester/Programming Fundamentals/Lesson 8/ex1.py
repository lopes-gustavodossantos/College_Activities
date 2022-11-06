import os

os.system("cls")
n = int(input("Informe um valor: "))

while n > 0:
    n -= 1
    frase = input("Informe a frase: ")
    m = int(len(frase) / 2) - 1
    saida = frase[m : : -1] + frase[len(frase) - 1 : m :-1]
    print(saida)
