from itertools import chain, zip_longest, product, combinations, permutations,cycle

#chain
seq1 = (1, 2, 3)
seq2 = ['a', 'b', 'c']

for elemento in chain(seq1, seq2):
    print(elemento)
print()
for elemento in chain(seq1, seq2, seq2, seq2):
    print(elemento)
print()

#zip_longest
nomes = ['Fábio','Suelem','Eduardo','Sofia']
idades = [47, 44, 19, 15]
cpfs = ['xxx','yyy','zzz']
emails = ['fabio@empresa.com','suelem@empresa.com']

for elemento in zip_longest(nomes, idades, cpfs, emails):
    print(elemento)
print()

for elemento in zip_longest(nomes, idades, cpfs, emails, fillvalue=''): # Pode passar qualquer coisa que queira
    print(elemento)
print()

# product
comidas = ['Churrasco', 'Pizza', 'Sushi']
bebidas = ['Refigerante', 'Água']

for prato in product(comidas, bebidas): # faz todas as combinações existentes entre listas
    print(prato)
print()

# combinations
nomes = ['Marcos','Lucas','Rodrigo','Carlos']

for comb in combinations(nomes, 2):
    print(comb)
print()

# permutation
for comb in permutations(nomes, 2):
    print(comb)
print()

# cycle
'''
for cor in cycle(['azul','amarelo']): # infinito 
    print(cor)
    input()
'''
# e quando é util?
nomes = ['Marcos','Lucas','Rodrigo','Carlos']
equipes = ['E1','E2']

for nome, equipe in zip(nomes, cycle(equipes)):
    print(nome, equipe)
print()