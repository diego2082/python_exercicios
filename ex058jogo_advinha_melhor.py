from random import randint
num = randint(0,10)
#print(num)
acertou = False
cont=0
while not acertou:
    jog = int(input('Digite palpite: '))
    if jog> num:
        print('Menos...')
    elif jog< num:
        print('Mais...')
    cont = cont+1
    if jog == num:
        acertou=True
print(f'Acertou em {cont} tentativas. ')
