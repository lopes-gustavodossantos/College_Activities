# 28) O Hipermercado Tabajara está com uma promoçãp de carnes que é imperdível. Confira:
#                          Até 5 Kg      Acima de 5 Kg
#     File Duplo     R$ 4,90 por Kg     R$ 5,80 por Kg
#     Alcatra        R$ 5,90 por Kg     R$ 6,80 por Kg
#     Picanha        R$ 6,90 por Kg     R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de 
# carne comprada pelo usuário e gere um cupom fiscal, contendo aas informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

import os

os.system("cls")

tipo =  int(input("1 - Filé Duplo \n2 - Alcatra \n3 - Picanha \nInforme qual tipo de carne você deseja: "))
quantidade = float(input("Informe a quantidade de carne desejada: ").replace(",", "."))
pagamento = int(input("O pagamento será feito utilizadando um cartão Tabajara? \n1 - SIM \n2 - NÃO \nInforme: "))
linha_cupom = '=' * 10
linha_fim = '=' * 34

if tipo == 1:
    carne = "Filé Duplo"
    if quantidade <= 5:
        valor = quantidade * 4.90
    else:
        valor = quantidade * 5.80
        
if tipo == 2:
    carne = "Alcatra"
    if quantidade <= 5:
        valor = quantidade * 5.90
    else:
        valor = quantidade * 6.80
        
if tipo == 3:
    carne = "Picanha"
    if quantidade <= 5:
        valor = quantidade * 6.90
    else:
        valor = quantidade * 7.80
        
if pagamento == 1:
    cartao = "SIM"
    desconto = valor * 0.05
    total = valor - desconto 
else:
    cartao = "NÃO"
    desconto = 0
    total = valor
    
print(f'\n\n{linha_cupom} CUPOM FISCAL {linha_cupom}\nTipo: {carne} \nQuantidade: {quantidade} \nPreço total: {valor}\nCartão Tabajara: {cartao} \nDesconto de: R$ {desconto:.2f} \nPreço total com desconto: R$ {total:.2f} \n{linha_fim}\n\n')
