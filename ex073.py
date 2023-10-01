times = ('Botafogo','Palmeiras','RB Bragantino', 'Grêmio', 'Flamengo', 'Fluminense',
         'Athletico', 'Fortaleza',         'Atletico-MG', 'Cuiaba', 'Cruzeiro',
         'Internacional', 'São Paulo', 'Corinthians', 'Bahia',
         'Goias', 'Santos', 'Vasco', 'América-MG', 'Coritiba')
print('-=-' * 20)
print(f'Os 20 clubes são: {times}')
print('-=-' * 20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-' * 20)
print(f'Na zona de rebaixamento estão: {times[-4:]}')
print('-=-' * 20)
print(f'Ordem alfabética: {sorted(times)}')
print('-=-' * 20)
print(f'Corinthians se encontra na {times.index("Corinthians")+1}ª posição')


