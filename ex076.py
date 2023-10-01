nome_de_produtos = ('Camiseta', 39.9,
                    'Calça Chino', 119.9,
                    'Tenis Air Force', 799.,
                    'Jaqueta Sarja', 79.49,
                    'Meia', 39.9,
                    'Cueca Lupo', 15.79,
                    'Tenis Vans Ultrarange', 99.9,
                    'Camisa Henley', 69.59,
                    'Bota masculina', 149.49)
print('_'*40)
print(f'{"LISTA DE PREÇOS OUTLETPREMIUM":^40}')
print('_'*40)
for pos in range(0, len(nome_de_produtos)):
    if pos % 2 == 0 :#POSIÇÃO PAR PARA AS STRING COM NOME DOS PRODUTOS
        print(f'{nome_de_produtos[pos]:.<30}',end='')
    else:#POSIÇÃO IMPAR PARA OS VALORES EM R$
        print(f'R${nome_de_produtos[pos]:>7.2f}')

print('_'*40)