val = list()
for cont in range(0,5):
    n = (int(input('Digite um valor para posição: ')))
    if cont == 0:#primeiro loop, posiçao 0;
        val.append(n)
    elif n > val[-1]:#maior valor na ultima posição da lista
        val.append(n)
        print('Adicionado ao final da lista..')
    else:
        pos=0
        while pos < len(val):
          if n <= val[pos]:
            val.insert(pos, n)
            print(f'Adicionado na posição {pos} da lista..')
            break
          pos+=1

print(val)
