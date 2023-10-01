num =soma= media =quant= maior= menor =0
resp= 'S'
print('~*'*30)
while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior=menor =num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar?[S/N] ')).strip().upper()
media = soma /quant
print('~*'*30)
print(f'A média dos valores é {media}, com maior valor sendo {maior}, e o menor sendo {menor}')


