lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not  in 'SN':
     continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if continuar == 'N':
         break
print('-~'*15)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 not in lista:
        print('O número 5 não foi encontrado na lista.')
else:
        print('O número 5 esta na lista.')


