palavras = ('canto','realiza', 'teclado', 'aula', 'faculdade', 'sistemas', 'desenvolvimento',
            'mercado', 'simples', 'relatividade')

for vog in palavras:#percorrer a tupla de palavras encontando vogais
    print(f'\nNa palavra {vog} temos ',end='')
    for letra in vog:
        if letra.lower() in 'aeiou' :
            print(letra,end=' ')
