'''detector de PALÍNDROMO'''
frase = str(input('Digite a frase: ')).strip().upper()
palavra = frase.split()#DIVIDIR PARA GERA LISTA
junto = ''.join(palavra)#JUNTA A LISTA ELIMINANDO ESPAÇOS

inverso = ''
for letra in range(len(junto)-1,-1,-1):#PERCORREU PRINTANDO DO FIM PARA COMEÇO
    inverso=inverso+junto[letra]
print(inverso, junto)
if inverso == junto:#
    print('É um palídromo!')
else:
    print('Não é palíndromo!')

    #inverso = junto[::-1] -> fatiamento de string'''