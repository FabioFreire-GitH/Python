a = {1,2,3,4} #conjunto em python (set)
print(a)
print(type(a))
b = set([3,4,5,6,7])
print(b)
# Conjuntos nao podem ter elementos duplicados
c = {1,2,2,1,2,1,1,1,2,1}
print(c)
c.add(3)
print(c)
print()
numeros = [1,2,3,4,1,2,3,1,2,4,2,1,1,5,2] # LISTA de numeros
print(numeros)
numeros_unicos = list(set(numeros)) # converte a lista em conjunto e depois novamente em lista
print(numeros_unicos)
print()

# Não há ordem num conjunto entao nao tem como fazer um busca num elemento desta forma: a[0]
a = {10, 'Python', 1.0, False}
#a[0] # dará erro typeError
for elemento in a:
    print(elemento)
print()
a = {(1,2,3)}
print(a)
print()
a = {1,2,3,4}
b = {3,4,5,6,7}
print(a.union(b))
print(a | b)
print()
print(a.intersection(b))
print(a & b)
print()
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)
print()
print(a.symmetric_difference(b))
print((a - b) | (b - a))
print()
#numeros = list(range(1000))
print(numeros) # uma busca por um elemento numa lista é muito mais lento que em um conjunto.












