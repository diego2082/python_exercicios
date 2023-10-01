print('-='*17)
print('** Sequência Fibonacci **')
print('-='*17)
num = int(input('Quantos termos mostrar? '))
t1=0
t2=1
print(f'{t1}, {t2}',end='')
c = 3
while c <= num:
    t3 = t1 + t2
    print(f', {t3}',end='')
    c=c+1
    t1 = t2
    t2 = t3
print('\nSequência encerrada',end='')



