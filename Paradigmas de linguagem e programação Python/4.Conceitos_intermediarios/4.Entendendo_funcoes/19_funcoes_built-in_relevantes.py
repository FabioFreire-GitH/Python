# isinstance
print()
valor = 2
if isinstance(valor, int):
    print('Valor é do tipo int')
else:
    print('Valor não é do tipo int')
print()

valor = 'Oi'
if isinstance(valor, int):
    print('Valor é do tipo int')
else:
    print('Valor não é do tipo int')
print()

valor = True
if isinstance(valor, int):
    print('Valor é do tipo int')
else:
    print('Valor não é do tipo int')

print()
valor = 10.5
if isinstance(valor, (int, float)):
    print('Valor é do tipo númerico')
else:
    print('Valor não é do tipo númerico')

#any e all
print()
booleanos = [True, True, False]
print(all(booleanos))
print(any(booleanos))
print(not all(booleanos))
print(not any(booleanos))
print()

valores = [1, 2, 2.5, 3]
if all(isinstance(valor, int) for valor in valores):
    print('Todos os valores são int')
else:
    print('Nem todos os valores são int')

if any(isinstance(valor, int) for valor in valores):
    print('Pelo menos um valor é int')
else:
    print('Nenhum valor é int')
print()

#map
def somar_dois(n):
    return n + 2

numeros = [3, 6, 10]
mapa = map(somar_dois, numeros)
print(mapa)
print(list(mapa))
# (map) não é tão usado mais, devido a compreensão de listas. Conforme abaixo:
numeros_mais_dois = [somar_dois(n) for n in numeros]
print(numeros_mais_dois) 

#filter (semelhante a map)
def meu_filtro(n):
    return n > 5

numeros = [3, 6, 10]
filtro = filter(meu_filtro, numeros)
print(filtro)
print(list(filtro))

#em compreensao de lista
maiores_que_cinco = [n for n in numeros if meu_filtro(n)]
print(maiores_que_cinco)
