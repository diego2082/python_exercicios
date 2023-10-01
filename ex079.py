valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!..')
    else:
        print('Valor já existe na lista')

    c = str.upper(input('Quer continuar? S/N '))
    if c in 'N':
        break

print(f'Você digitou os valores {sorted(valores)}')

