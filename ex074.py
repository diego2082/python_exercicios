from random import randint
num = randint(1,10), randint(1,10), randint(1,10), randint(1,10),randint(1,10)
print('Os números sorteados são: ' , end="")

for n in num:
    print(f'{n} | ',end='')
print(f'\nO menor deles é: {min(num)}')
print(f'O maior deles é: {max(num)}')

