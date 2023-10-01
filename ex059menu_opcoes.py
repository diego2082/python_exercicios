from time import sleep
valor1 = int(input('1º Valor: '))
valor2 = int(input('2º Valor: '))
opcao = 0
while opcao != 5:
    print('-='* 15)
    print('''    [1]- Somar
    [2]- Multiplicar
    [3]- Maior
    [4]- Novos Números
    [5]- Encerrar ''')
    print('-='* 15)
    opcao = int(input('Digite sua opção: '))
    if opcao > 5 or opcao<= 0:
        print('Opção inválida! Tente novamente.')
    elif opcao == 1:
        soma = valor1+valor2
        print(f'A soma de {valor1} e {valor2} é: {soma}')
    elif opcao == 2:
        multiplica = valor1 * valor2
        print(f'A multiplicação de {valor1} e {valor2} é: {multiplica}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        else:
            print(f'O maior valor é {valor2}')
    elif opcao == 4:
        print('Digite os novos valores: ')
        valor1 = int(input('1º Valor: '))
        valor2 = int(input('2º Valor: '))
print('Encerrando',end='')
sleep(1.4)
print('.',end='')
sleep(1.4)
print('.',end='')
sleep(1.4)
print('.',end='')
sleep(1.4)
print('Fim')
