matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):#para cada linha de 0 a 2
    for c in range(0,3):#para cada coluna de 0 a 2
        matriz[l][c]= int(input(f'digite valor [{l},{c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ] ',end='')
    print()