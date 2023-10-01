maior_idade_homem = 0
nome_velho = ''#VARIÁVEL RECEBE ESPAÇO EM BRANCO, ONDE VAI RECEBER NOME DURANTE O LAÇO DE REPETIÇÃO;
soma_idade = 0 #VARIÁVEL QUE VAI ARMAZENAR A SOMA DAS IDADES FORNECIDAS PELO USIÁRIO;
mulher_20 = 0
for cont in range(1,5):
    print('-='*15)
    nome =str(input(f'Digite nome da {cont}ª pessoa: ')).strip()
    idade=int(input('Digite a idade: '))
    sexo = str(input('Qual sexo da pessoa: M/F ')).upper().strip()
    soma_idade = soma_idade + idade
    if cont == 1 and sexo in 'Mm':#SE CONTADOR FOR A PRIMEIRA PESSOA E MASCULINO;
        maior_idade_homem=idade
        nome_velho=nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem=idade
        nome_velho=nome
    if sexo in 'Ff' and idade <20:
        mulher_20 = mulher_20+1
media = soma_idade / 4
print(f'A média de idade da lista é {media}')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}')
print(f'Total de {mulher_20} mulheres abaixo de 20 anos')