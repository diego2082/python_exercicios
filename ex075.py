num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')), int(input('Digite último número: ')))
print(f'Você digitou os valores: {num}')
if 9 in num:
    print(f'O valor 9  apareceu {num.count(9)} vezes')
else:
    print('O valor 9 não foi digitado dessa vez')
    if 3 in num:
        print(f'O primeiro valor 3 apareceu na {num.index(3)+1}ª posição')#quando digitado valor 3 a função
    else:                                         ################################################################### .index() da posição do elemento na tupla
       print('O valor 3 não foi digitado dessa vez')
    print(f'Os valores pares digitados foram: ',end='')
    for n in num:
        if n % 2 == 0:
            print(n, end=' ')




