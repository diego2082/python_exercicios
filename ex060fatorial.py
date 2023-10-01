from  math import factorial
n = int(input('Digite para fatorial: '))
c = n
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else' = ',end='')
    c = c - 1
    f = factorial(n)
print(f'{f}')
