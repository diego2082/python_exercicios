prim_termo = int(input('Digite o 1º termo: '))
raz = int(input('Digite a razão do termo: '))
termo = prim_termo
c=1
total = 0
mais = 10
contador=0
while mais != 0:#LAÇOS ANINHADOS
    total=total+mais
    while c <= total:
            print(f'{termo}->',end=' ')
            termo= termo+raz
            c = c + 1
    print('PAUSA',end='')
    mais=int(input('\nQuantos mais termos quer ver: '))
print(f'Finalizado com {total} termos mostrados')








