while True:
    try:
        a,b,c = list(map(int,input("Informe a escolha de cada participante, utilizando um espaço!\nOrdem de jogo: Alice, Beto, Clara\nEscolhas: ").split()))
        
        if(a == b == c):
            print("*")
        else:
            if(a == b):
                print("C")
            else:
                if(a == c):
                    print("B")
                else:
                    print("A")

    except (EOFError):
        break
