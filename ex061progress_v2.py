prim_termo = int(input('Digite o 1º termo: '))
raz = int(input('Digite a razão do termo: '))
termo = prim_termo
c=1
while c <= 10:
        print(f'{termo}->',end=' ')
        termo= termo+raz
        c = c + 1
print('FIM')




