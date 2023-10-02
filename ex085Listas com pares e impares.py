#temp = list()
#princ = list()
#for c in range(1,8):
 #   temp.append(int(input(f'Digite o {c}º valor: ')))
  #  princ.append(temp[:])
   # temp.clear()
    #princ.sort()
#print('Os valores pares são: ', end='')
#for n in princ:
 #       if n[0] % 2 == 0:
  #          print(f'{n[0]}, ',end='')
#print()
#print('Os valores impares são: ',end='')
#for n in princ:
 #   if n[0] % 2 != 0:
  #      print(f'{n[0]}, ', end='')




num = [[],[]]#LISTA COMPOSTA DE 2 LISTAS INTERNAS: 0 E 1#
valor = 0
for c in range(1,8):
    valor = (int(input(f'Digite o {c}º valor: ')))
    if valor % 2 == 0:
        num[0].append(valor)#para cada valor lido, se condição par for verdadeiro, .append para lista da lista 0
    else:
        num[1].append(valor)#para cada valor lido, se condição par for falso, .append para lista da lista 1
#colocando em ordem crescente
num[0].sort()
num[1].sort()
print()
print(f'Os valores pares são: {num[0]}')
print(f'Os valores impares são: {num[1]}')



