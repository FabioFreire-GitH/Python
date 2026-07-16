seq = (10, 20, 30)
a, b, c = seq
print(a, b, c)
print()

dic = {
    'chave1':'valor1',
    'chave2':'valor2',
    'chave3':'valor3',
}

for chave, valor in dic.items():
    print(chave, valor)
print()

nomes = ['Fábio','Suelem','Eduardo','Sofia']
idades = [47, 44, 19, 15]

for elemento in enumerate(zip(nomes, idades)):
    print(elemento)
print()

for i, (nome, idade) in enumerate(zip(nomes, idades)):
    print(i, nome, idade)
print()

minha_lista = [1, 2, 3, 4, 5]
primeiro, *meio, ultimo = minha_lista
print(primeiro, ultimo)
print(meio)
print()

primeiro, *resto = (1,2,3,4) #Usando esse asteristico sempre retorna uma lista
print(primeiro)
print(resto)
print()

primerio, *meio, ultimo = (1,2)
print(primeiro, ultimo)
print(meio)
print()

primeiro, *_, ultimo = (1,2,3,4)

