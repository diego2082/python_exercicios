peso = list()
for cont in range(1,6):
    peso.append(float(input(f'Peso da {cont}ª pessoa:')))
    maior_peso= max(peso)
    menor_peso = min(peso)

print(f'A pessoa mais pesada tem {maior_peso}Kg')
print(f'A pessoa mais leve tem {menor_peso}Kg')

#maior = 0
#menor = 0
#for p in range(1,6):
#   peso = float(input(f'Peso da {p}ª pessoa'))
    #   if p == 1:
#       maior = peso
#       menor = peso
#   else:
#       if peso > maior:
#           maior = peso
#       if peso < menor:
#           menor = peso
#print(f'A pessoa mais pesada tem {maior}Kg')
#print(f'A pessoa mais leve tem {menor}Kg')
