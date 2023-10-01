total_pessoas= 0
total_homem = 0
total_mulher20=0
while True:
    sexo = ' '
    idade = int(input('Idade?: '))
    while sexo not in 'fFMm':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        total_pessoas += 1
    if sexo == 'M':
        total_homem +=1
    if sexo == 'F':
        if idade < 20:
            total_mulher20 +=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-~'*30)
print(f'Total pessoas 18+ é: {total_pessoas}')
print(f'Total de homens é: {total_homem}')
print(f'Total de mulheres menores de 20 é: {total_mulher20}')
print('-~'*30)