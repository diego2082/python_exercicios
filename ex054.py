#PROGRAMA QUE VERIFICA QUEM É MAIOR E MENOR DE IDADE
from datetime import date
atual = date.today().year
total_maior=0
total_menor=0
for pess in range(1,8):
    nasc = (int(input(f'Em que ano a {pess}ª pessoa nasceu: ')))
    idade = atual-nasc
    if idade  >= 21:
        total_maior = total_maior + 1
    else:
            total_menor = total_menor + 1
print('-='*30)
print(f'{total_maior} pessoa(s) são maior(es) de idade')
print(f'{total_menor} pessoa(s) são menor(es) de idade')
print('-='*30)