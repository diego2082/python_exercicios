lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not  in 'SN':
     continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if continuar == 'N':
         break
for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('-~'*15)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
