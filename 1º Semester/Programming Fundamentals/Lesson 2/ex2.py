# 2) Variáveis + Print:

nome = "Roberto"
sobrenome = "da Silva Santos"
cidade = "Florianópolis"
estado = "Santa Catarina"
print(f'\n{nome} {sobrenome} mora na cidade de {cidade} no estado de {estado}.') 

# 2.1) Variáveis + Print + Upgrade:
                                            
nome = str(input("Digite seu nome: ").title())                                
sobrenome = str(input("Digite seu sobrenome: ").title())                       
cidade = str(input("Digite o nome da cidade onde mora: ").title())             
estado = str(input("Digite o nome do estado onde mora: ").title())             
print(f'\n{nome} {sobrenome} mora na cidade de {cidade} no estado do {estado}.') 
