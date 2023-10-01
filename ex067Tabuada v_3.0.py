cont = 0
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
            break
    for cont in range(0,11):
                print(f'{num} X {cont} = {num * cont}')
    print('=-' * 30)
    cont += 1
print('FIM...')
