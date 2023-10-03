matriz = [[0,0,0],[0,0,0],[0,0,0]] #matriz de 9 posições com atribuição zero
maiorvalor= somapar = somacol = 0
for l in range(0,3):#Loop para preenchimento da matriz
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite o valor para [{l},{c}]: '))
print()
for l in range(0,3):#Imprimindo em estilo tabela
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ] ',end='')
    print()#A cada 3 posições pular linha
for l in range(0,3):#Encontrar e somar numeros pares se houverem
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
           somapar +=matriz[l][c]
print()
for l in range(0,3):#Somar valores especifico da coluna 3
    somacol=somacol+matriz[l][2]
print()
for c in range(0,3):#Identificar o maior valor da segunda linha
       if c  == 0:
        maiorvalor = matriz[1][c]
       else:
           if matriz[1][c] > maiorvalor:
               maiorvalor= matriz[1][c]
print()
print(f'A soma dos pares é {somapar}.')
print(f'A soma da última coluna é {somacol}')
print(f'O maior valor da segunda linha é {maiorvalor}.')






