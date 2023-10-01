lista = list()
lista = str(input('Digite expressão: '))
par1 = lista.count("(")
par2 = lista.count(")")
if par1 % 2 == 0  and par2 % 2 == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')
