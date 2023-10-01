dados = list()#LISTA TEMPORÁRIA
galera = list()#LISTA PRINCIPAL
maiorpeso = menorpeso = 0
while True:#LER OS DADOS EM LOOP ATÉ DECIDIR PARAR#
    dados.append(str(input('Nome: ')))#DADOS[0]
    dados.append(float(input('Peso: ')))#DADOS[1]
    continua = ' '
    if len(galera) == 0:#SE FOR PRIMEIRO DADO ENTAO:
        maiorpeso=menorpeso=dados[1]
    else:
                if dados[1] > maiorpeso:
                    maiorpeso = dados[1]
                if dados[1] < menorpeso:
                    menorpeso = dados[1]
    galera.append(dados[:])#ADICIONA COPIA PARA LISTA PRINCIPAL E DELETA TEMPORÁRIA
    dados.clear()
    while continua not in 'SN':
        continua = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if continua == 'N':
            break
print(f'Total de pessoas é {len(galera)}')#TOTAL DE LOOPS
print(f'O maior peso é: {maiorpeso}Kg',end='')
for p in galera:#PERCORRER VETOR EM BUSCA DO MAIOR PESO, PODE SER MAIS DE 1.
    if p[1] == maiorpeso:
        print(f' [{p[0]}]',end='')
print()
print(f'O menor peso é: {menorpeso}Kg', end='')
for p in galera:#PERCORRER EM BUSCA DO MENOR, PODE HAVER MAIS DE 1.
    if p[1] == menorpeso:
        print(f' [{p[0]}]', end='')








