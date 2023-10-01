num = 0
cont = 0
soma = 0
num = int(input('Digite valor [999 to stop]: '))
while num != 999:
    cont +=1
    soma = soma + num
    num = int(input('Digite valor [999 to stop]: '))
print(f'Foram digitados {cont} valor(es) que somados são {soma }')


