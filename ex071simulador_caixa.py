
saque = int(input('Qual valor a ser sacado R$: '))
while  saque % 5 != 0:
    print('Não há nota disponível! Tente novamente.')
    saque = int(input('Qual valor a ser sacado R$: '))

total = saque
ced = 200
totced = 0
while True:
        if total >= ced:
            total= total - ced
            totced = totced + 1
        else:
            if totced > 0:
             print(f'{totced} Nota(s) de {ced} reais')
            if ced == 200 :
                ced=100
            elif ced == 100:
                ced=50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5



            totced = 0
            if total == 0 :
                break






