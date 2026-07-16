#Desafio 01
#Crie uma função que retorna os valores de duas listas de forma intercalada, mesmo quando as listas
#têm tamanho diferente. Por exemplo, dadas as listas:
from itertools import zip_longest, product

L1 = [1,2,3]
L2 = ['a','b','c','d','e']

def retorna_intercalado(lista1,lista2):
    resultado = []
    for valor1, valor2 in zip_longest(lista1, lista2):
        if valor1 is not None:
            resultado.append(valor1)
        if valor2 is not None:
            resultado.append(valor2)
    return resultado

print(retorna_intercalado(L1,L2))
print()

#Desafio 02
#Imagine que você tem um restaurante com os seguintes itens no seu menu:

comidas = {
'Prato Feito': 24.90,
'Salada': 21.90,
'Strogonoff': 29.90,
'Feijoada': 32.90,
}
bebidas = {
'Água': 3.90,
'Refrigerante': 5.90,
'Suco': 7.90,
}

#Crie um novo dicionário chamado combos onde cada chave é uma tupla contendo (comida,
#bebida), e o seu respectivo valor é o preço daquela combinação de comida e bebida.

#forma tradicional
combos = dict()
'''
for chave_comida, preco_comida in comidas.items():
    for chave_bebida, preco_bebida in bebidas.items():
        chave_combo = (chave_comida, chave_bebida)
        preco_combo = preco_comida + preco_bebida
        combos[chave_combo] = round(preco_combo, 2)
print(combos)
'''
print()

# forma 2
'''
for chave_combo in product(comidas, bebidas):
    chave_comida, chave_bebida = chave_combo
    preco_combo = comidas[chave_comida] + bebidas[chave_bebida]
    combos[chave_combo] = round(preco_combo,2)
print(combos)
'''

# forma 3
for tupla in product(comidas.items(), bebidas.items()):
    #print(tupla)
    chave_combo = tuple(tup[0] for tup in tupla)
    #print(chave_combo)
    preco_combo = sum(tup[1] for tup in tupla)
    #print(preco_combo)
    combos[chave_combo] = round(preco_combo,2) 
print(combos)
    