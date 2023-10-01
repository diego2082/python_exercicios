from random import randint
vit = 0
while True:#looping infinito
    num=int(input('Digite um número: '))
    maq = randint(0, 10)
    escolha=' '
    soma = num + maq
    while escolha not in 'PpIi':#enquanto escolha não estiver dentro de p ou i.
            escolha = str(input('Escolha PAR ou IMPAR [P/I]: ')).upper().strip()[0]
    print(f'Você escolheu {num} e o PC escolheu {maq}. Total {soma}',end='')
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'. A soma é {soma}, então é PAR e você ganhou!. ')
            vit+=1
        else:
            print(f'. A soma é {soma}, então é IMPAR e vc perdeu!! . ')
            break

    elif escolha == 'I':
        if soma % 2 == 1:
            print(f'. A soma é {soma}, então é IMPAR e você ganhou!. ')
            vit+=1
        else:
            print(f'. A soma é {soma}, então é PAR e vc perdeu!!. ')
            break
    print('Continue jogando...')
print(f'Fim de jogo e você venceu {vit} vez(es)!')











