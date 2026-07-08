# Aula 17: LISTAS (Variaveis Compostas) PARTE 1 - usa Colchetes []
# AS LISTAS SÃO MUTAVEIS. 

lanche = ['Hambúrguer','Suco','Pizza','Pudim'] # LISTA

print()
print(lanche)

#Adicionar elemento
lanche.append('Cookie')
print(lanche)
lanche.insert(0, 'Batata frita')
print(lanche)
#Deletar elemento
#metodo 1 : del lanche[3] 
#metodo 2 : lanche.pop(3) #Normalmente é usado para eliminar o ultimo elemento, mas pode passar como parametro o indice para remover
#metodo 3 : lanche.remove('Pizza')  #Aqui voce nao indica o indice e sim o conteudo
# A remoçao tambem reposiciona
lanche.pop(3)
print(lanche)
if 'Pizza' in lanche: # Aqui so remove se encontrar, trata erro caso o item não exista
    lanche.remove('pizza')
valores = list(range(4,11))# declara um lista dos elementos 4 a 10 numa lista valores de indice 0 a 6 (7 elementos)

numeros = [8,2,5,4,9,3,0]
print(numeros)
numeros.sort() #em ordem
print(numeros)
numeros.sort(reverse=True)
print(numeros)
print(len(numeros))
print()
num_tupla = (2,5,9,1)
print(num_tupla)
num_lista = list(num_tupla)
print(num_lista)
num_lista[2] = 7
print(num_lista)
num_lista.append(4)
print(num_lista)
num_lista.sort()
print(num_lista)
num_lista.pop()
print(num_lista)
num_lista.insert(2, 6)# na posicao tal, o valor tal
print(num_lista)
num_lista.insert(0, 0)
print(num_lista)
num_lista.sort(reverse=True)
print(num_lista)
print()

num_lista = list()
num_lista.append(5)
num_lista.append(9)
num_lista.append(4)
print(num_lista)
for c, n in enumerate(num_lista): #O enumerate pega tanto a chave(posicao) quanto o valor(elemento)
    print(f'Na posição {c} enccontrei o valor {n}!')
print('\nFim da lista\n')


num_lista = list()
for cont in range(0, 5):
    num_lista.append(int(input('Digite um valor: ')))
print(num_lista)
for c, n in enumerate(num_lista): #O enumerate pega tanto a chave(posicao) quanto o valor(elemento)
    print(f'Na posição {c} enccontrei o valor {n}!')
print('\nFim da lista\n')

a = [2, 3, 4, 7]
b = a # cria uma ligacao entre listas
b[2] = 8
print(a)
print(b)

print()

a = [2, 3, 4, 7]
b = a[:] # cria uma copia
b[2] = 8
print(a)
print(b)





