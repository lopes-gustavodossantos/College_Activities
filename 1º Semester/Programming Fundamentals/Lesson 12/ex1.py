n = int(input(""))
m = int(input(""))

def get_align(matriz, coluna):
    column = []
    for i in range(len(matriz)):
        column.append(matriz[i][coluna])
    column.sort(reverse=True)
    return len(str(column[0]))

matrizes = [[[int(i)**2 for i in input().split()] for i in range(m)] for i in range(n)]

cont = 4

for i in matrizes:
    print("Quadrado da matriz #%d:" % cont)
    for j in range(m):
        for k in range(m):
            print(" " * (get_align(i, k) - len(str(i[j][k]))), i[j][k], end = ' ', sep='')
        print('')
    print('')
    cont += 1
