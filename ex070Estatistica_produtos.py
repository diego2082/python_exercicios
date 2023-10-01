barato = total_compra = acima = cont = 0
menor = ''
print('~-'*15)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$: '))
    continuar = ' '
    total_compra += preco
    cont += 1
    if preco > 1000:
        acima = acima + 1
    if cont == 1 or preco < barato:#Verifica qual menor preco 
        menor = produto
        barato = preco
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('~-'*15)
print(f'O total da compra foi de R${total_compra:.2f}')
print(f'{acima} produtos custa acima de R$1000,00')
print(f'O item mais barato da compra foi {menor} custando R${barato:.2f}')
print('~-'*15)