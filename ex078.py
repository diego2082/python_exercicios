valores = list()
for cont in range(0,5): #laço para entrar com dados nas posições da lista
    valores.append(int(input(f'Digite um valor para posição {cont}: ')))
    maior = max(valores)#função para armazenar o maior valor digitado pelo usuario
    menor = min(valores)#Função para armazenar o menor valor

print(f'Você digitou os valores {valores}')
print(f'O(s) maior(es) valor(es) foi {maior} na posição ',end='')
for chave, valor in enumerate(valores):# laço com função para percorrrer variavel valores e
    if valor == maior:                                                                                                                        #                #imprimir posição na list do maior
        print(f'{chave}..')

print(f'O(s) menor(es) valor(es) foi {menor} na posição ', end='')
for chave, valor in enumerate(valores):
            if valor == menor:
                print(f'{chave}..')
