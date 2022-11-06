import csv, time, os

def cleanScreen():
    time.sleep(3)
    os.system("cls")

periodic_table = {}
states = {'l': 'Líquido', 'g': 'Gasoso', 's': 'Sólido', 'd': 'Desconhecido'} 

file = csv.reader(open('S2_Tabela_Periódica.txt'), delimiter=';')

for i, line_data in enumerate(file):
    if i == 0:
        continue

    data = {}
    data['simbolo'] = line_data[0]
    data['nome'] = line_data[1]
    data['numero_atomico'] = line_data[2] 
    data['linha'] = line_data[3] 
    data['coluna'] = line_data[4] 
    data['estado'] = line_data[5]
   
    periodic_table[data['simbolo']] = data

while True:
    os.system("cls")
    
    print(("=" * 24))
    print(" " * 3, "TABELA PERIÓDICA")
    print("=" * 24)

    print("Elementos disponíveis: Al Au Br H O\nSelecione uma das opções:\n1 - Listar todos os Elementos\n2 - Listar todos os dados de um Elemento\n3 - Listar dados específicos de um Elemento\n0 - Sair")

    while True:   
        try:
            option = int(input("\nOpção: "))
            if option in (0,1,2,3):
                break
            else:
                print("Opção Inválida\nDigite novamente!")
        except ValueError:
            print("Apenas números são aceitos!")

    if option == 1:
        print(periodic_table)
        cleanScreen()
        
    elif option == 2:
        element = input("Digite o símbolo de um Elemento: ")
        if element in periodic_table:            
            print(f"\nSímbolo: {element}")
            print(f"Nome: {periodic_table[element]['nome']}")
            print(f"Nº. Atômico: {periodic_table[element]['numero_atomico']}")
            print(f"Linha: {periodic_table[element]['linha']}")
            print(f"Coluna: {periodic_table[element]['coluna']}")

            state = states[periodic_table[element]['estado']]
            print(f"Estado: {state}")
        else:
            print("Elemento não disponível!")

    elif option == 3:
        element = input("Digite o símbolo de um Elemento: ")
        print("\nEscolha um dado específico:\n1 - Nome do Elemento\n2 - Número Atômico\n3 - Linha e Coluna\n4 - Estado")

        while True:            
            try:
                specific_option = int(input("Opção: "))
                if specific_option in (1,2,3,4):
                    break
                else:
                    print("Opção Inválida\nDigite novamente!")
            except ValueError:
                print("Apenas números são aceitos!")

        print("")
        
        if specific_option == 1:
            print(f"Nome: {periodic_table[element]['nome']}")
            cleanScreen()
            
        elif specific_option == 2:
            print(f"Nº. Atomico: {periodic_table[element]['numero_atomico']}")
            cleanScreen()
            
        elif specific_option == 3:
            print(f"Linha: {periodic_table[element]['linha']}\nColuna: {periodic_table[element]['coluna']}")
            cleanScreen()
            
        elif specific_option == 4:
            state = states[periodic_table[element]['estado']]
            print(f"Estado: {state}")
            cleanScreen()
                
    elif option == 0:
        break
