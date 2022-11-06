# 25) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#       a. "Telefonou para a vítima?"
#       b. "Esteve no local do crime?"
#       c. "Mora perto da vítima?"
#       d. "Devia para a vítima?"
#       e. "Já trabalhou com a vítima?"
# O programa deve no finaç emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

import os

os.system("cls")

p1 = int(input("Responda as perguntas a seguir utilizando somente:\n1 - SIM \n2 - NÃO\nTelefonou para a vítima? "))
p2 = int(input("Esteve no local do crime? "))
p3 = int(input("Mora perto da vítima? "))
p4 = int(input("Devia para a vítima?"))
p5 = int(input("Já trabalhou com a vítima? "))
teste = 0

if p1 == 1:
    teste = teste + 1
else:
    teste = teste + 0
    
if p2 == 1:
    teste = teste + 1
else:
    teste = teste + 0
    
if p3 == 1:
    teste = teste + 1
else:
    teste = teste + 0
    
if p4 == 1:
    teste = teste + 1
else:
    teste = teste + 0
    
if p5 == 1:
    teste = teste + 1
else:
    teste = teste + 0
    
if teste == 2:
    print("\nClassificação: Suspeita")
elif teste == 3 or teste == 4:
    print("\nClassificação: Cúmplice")
elif teste == 5:
    print("\nClassificação: Assassino")
else:
    print("\nClassificação: Inocente")
