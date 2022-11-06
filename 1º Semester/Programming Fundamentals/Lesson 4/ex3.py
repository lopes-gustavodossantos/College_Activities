# 3) Algoritmo para auxiliar na correção do Jogo Pedra, Papel e Tesoura:

import random

opcoes = ["Pedra", "Papel", "Tesoura"]
jogador1 = random.choice(opcoes)
jogador2 = random.choice(opcoes)
print(f'\nJogador 1: {jogador1} \nJogador 2: {jogador2}')

if jogador1 == jogador2:                           
    print("\nEmpate!")
elif jogador1 == "Pedra" and jogador2 == "Papel":   
    print("\nO Jogador 2 é o vencedor!")
elif jogador1 == "Papel" and jogador2 == "Pedra":   
    print("\nO Jogador 1 é o vencedor!")
elif jogador1 == "Pedra" and jogador2 == "Tesoura":  
    print("\nO Jogador 1 é o vencedor!")
elif jogador1 == "Tesoura" and jogador2 == "Pedra":   
    print("\nO Jogador 2 é o vencedor!")
elif jogador1 == "Papel" and jogador2 == "Tesoura":  
    print("\nO Jogador 2 é o vencedor!")
elif jogador1 == "Tesoura" and jogador2 == "Papel":  
    print("\nO Jogador 1 é o vencedor!")

# 3.1) Algoritmo para auxiliar na correção do Jogo Pedra, Papel e Tesoura:
import random
import os
import time

while True:
    os.system("cls")
    
    jogador1 = str(input("Pedra\nPapel\nTesoura\nEscolha entre as opções acima: ").title())
    jogador2 = str(input("\nPedra\nPapel\nTesoura\nEscolha entre as opções acima: ").title())
    print(f'\nJogador 1: {jogador1} \nJogador 2: {jogador2}')
    if jogador1 == jogador2:                          
        print("\nEmpate!")
    elif jogador1 == "Pedra" and jogador2 == "Papel":  
        print("\nO Jogador 2 é o vencedor!")
    elif jogador1 == "Papel" and jogador2 == "Pedra":  
        print("\nO Jogador 1 é o vencedor!")
    elif jogador1 == "Pedra" and jogador2 == "Tesoura": 
        print("\nO Jogador 1 é o vencedor!")
    elif jogador1 == "Tesoura" and jogador2 == "Pedra":   
        print("\nO Jogador 2 é o vencedor!")
    elif jogador1 == "Papel" and jogador2 == "Tesoura":  
        print("\nO Jogador 2 é o vencedor!")
    elif jogador1 == "Tesoura" and jogador2 == "Papel": 
        print("\nO Jogador 1 é o vencedor!")
        
    time.sleep(5)
