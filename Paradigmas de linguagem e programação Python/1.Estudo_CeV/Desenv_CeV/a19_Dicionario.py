# Aula 19: DICIONÁRIOS (Variaveis Compostas) - usa Chaves {}

#Explicaçoes do Guanabara
print()
dados = dict()

dados = {'nome':'Pedro','idade':'25'} # aqui o indice é "personalizado", inves de indice numerico o indice pode possuir um string

print(dados['nome'])
print(dados['idade'])
print(dados)
print()

# adicionar no dicionario (o append nao funciona)
dados['sexo'] = 'M' #cria o elemento sexo e add ao dicionario automaticamente (o python chama os elementos de keys (chaves))
print(dados)
print()

#para remover
#com del
del dados['idade']
print(dados)
print()

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }
#Diferença entre itm, chave e valor
print(filme.values())
print(filme.keys())
print(filme.items())
print()

for k,v in filme.items():
    print(f'O {k} é {v}.')
print()

#Podemos juntar Listas, Tuplas e Dicionarios:

locadora = ({'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'},
         {'titulo':'Avengers',
         'ano':2012,
         'diretor':'Joss Whedon'},
         {'titulo':'Matrix',
         'ano':1999,
         'diretor':'Wachowski'})

print(locadora)
print()
print(locadora[0]['ano'])
print(locadora[2]['titulo'])
print()

#Parte Pratica

print('-='*30)
print('{:^60}'.format('PARTE PRÁTICA - 1'))
print('-='*30)
print()

pessoas = {'nome': 'Fabio', 'idade': 47, 'sexo': 'M'} # dicionario

print(pessoas['nome'])
# ATENÇÃO
print(f'O {pessoas["nome"]} em {pessoas["idade"]} anos.') # no print formatado é necessario aspas duplas "", pois ficaria aspas simples dentro de aspas simples e nao funcionaria. (pois abre e fecha)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k in pessoas.items():
    print(k)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()


#Criando dicinario dentro da lista
print('-='*30)
print('{:^60}'.format('PARTE PRÁTICA - 2'))
print('-='*30)
print()

estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print()

print('-='*30)
print('{:^60}'.format('PARTE PRÁTICA - 3'))
print('-='*30)
print()
estado = dict()
bra = list()
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    bra.append(estado.copy())# fazer uma copia deve usar o metodo copy, pois o fatiamento[:] nao funciona, aqui é um dicionario. Tambem nao da pra deixar assim: bra.append(estado)
for e in bra:
    print(e)
print()
#fazendo mais "bonito"
for e in bra:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print()
for e in bra:
    for v in e.values():
        print(v, end=' ')
    print()
print()

