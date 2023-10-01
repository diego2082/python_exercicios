'''IMPRIMIR NÚMEROS primos'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m',end=' ')
        tot  +=1
    else:
        print('\033[31m',end=' ')
    print(c,end='   ')
print(f'\n-=-O numero {num} foi divisivel {tot} vezes.-=-')
if tot == 2:
    print('E é um número primo')
else:
    print('E não é um númereo primo')
