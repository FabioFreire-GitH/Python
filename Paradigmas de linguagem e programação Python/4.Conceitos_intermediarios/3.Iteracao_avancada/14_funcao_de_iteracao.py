#enumerate
nomes = ['Fábio','Suelem','Eduardo','Sofia']

for i, nome in enumerate(nomes):
    print(f'Índice {i} -> Nome {nome}')
print()

for i, nome in enumerate(nomes, 1):
    print(f'Posição da lista {i} -> Nome {nome}')
print()

for i, nome in enumerate(nomes, 100):
    print(f'Índice {i} -> Nome {nome}')
print()

#sorted
conj = {1, 10, -1, 4}
print(sorted(conj))
ordenados = sorted(conj)
print(ordenados)
print(conj)
ordenados = sorted(conj, reverse= True)
print(ordenados)
print()
lista1 =[1,10,-1,4]
lista2 = sorted(lista1)
print(lista2)
lista1.sort() # a lista ja tem um metodo sort embutido
print(lista1)
print()

#reversed
for i in reversed(range(10)):
    print(i)

#zip
nomes = ['Fábio','Suelem','Eduardo','Sofia']
idades = [47, 44, 19, 15]
cpfs = ['xxx','yyy','zzz']
emails = ['fabio@empresa.com','suelem@empresa.com']


for elemento in zip(nomes, idades):
    print(elemento)
print()
for elemento in zip(nomes, idades, cpfs, emails):
    print(elemento)


