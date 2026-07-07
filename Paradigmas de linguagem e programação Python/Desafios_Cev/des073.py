# desafio 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

classificacao = ('Palmeiras','Flamengo','Fluminense','Athletico-PR','Bragantino','Bahia','Coritiba','São Paulo','Atlético-MG','Corinthians','Cruzeiro','Botafogo','EC Vitória','Internacional','Santos','Grêmio','Vasco da Gama','Remo','Mirassol','Chapecoense')
print('\n{:^260}\n'.format('Classificação da Tabela 2026: (Parcial de Junho)'))
print('-='*130)
print(classificacao)
print('-='*130)
print('\n{:^260}\n'.format('Os Cinco Primeiro Colocados da Tabela'))
print('-='*130)
print(classificacao[0:6])
print('-='*130)
print('\n{:^260}\n'.format('Os Últimos 4 Colocados da Tabela'))
print('-='*130)
print(classificacao[16:])
print('-='*130)
print('\n{:^260}\n'.format('Em ordem Alfabetica '))
print('-='*130)
print(sorted(classificacao))
print('-='*130)
print('\n{:^260}\n'.format('Em que posição está o time da Chapecoense'))
print('-='*130)
print('A Chapecoense está na {}ª posição.'.format(classificacao.index('Chapecoense')+1))
print('-='*130)
print()