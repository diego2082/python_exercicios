num = cont = soma = 0
print('~*'*30)
while True:#LOOP INFINITO COM FLAG=999
    num = int(input('Digite valor [999 to stop]: '))
    if num == 999:
        break
    cont +=1
    soma = soma + num
print('~*' * 30)
print(f'Foram digitados {cont} valor(es) que somados são {soma }')


