# Aula 16: TUPLAS (Variaveis Compostas) - usa parênteses ()
# as TUPLAS são IMUTAVEIS. Uma vez definida, não é possivel mudar.
lanche = ('Hambúrguer','Suco','Pizza','Pudim','Batata frita') # TUPLA
print()
print(lanche)
print(lanche[2])
print(lanche[0:2]) # atenção ao fatiamento
print(lanche[1:])
print(lanche[-1])
print(lanche[0], lanche[-4])
print(lanche[-3:])
print(len(lanche))
print()
for c in lanche: #faz um loop, para cada c dentro de lanche (variavel) - Essa é uma outr forma de usar o for (para colecoes ou seja para variaveis composta como a Tupla). A outra forma vista anteriormente é o com range
    print(c)
print()

for comida in lanche:
    print(f'Eu comi {comida}')
print('Comi muito!!!')
print()

for cont in range (0, len(lanche)): 
    print(cont)
    print(lanche[cont])
    print()
print()

for posicao, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {posicao}')
print()

print(sorted(lanche)) #em ordem - NAO muda a ordem d variavel, somente exibe em ordem
print()

# Outros exmplos
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # "Cola" uma tupla com a outra e, c = a + b <> c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.count(9))
print(c.index(8)) # pega a posiçao em que esta o 8
print(c.index(2)) # pega a posição da primeira ocorrencia que esta o 2, pois nesta tupla c, tem dois numeros 2
print(c.index(5)) # tambem tem dois 5
print(c.index(5, 2)) # pega a partir da posiçao 2
print()
# mais exemplos

pessoa = ('Fabio',47,'M',102.60)
print(pessoa)
del(pessoa) #Apaga da memoria - TUPLA pode apagar tudo. Não smente um elemento como por exemplo del(pessoa[1])
print(pessoa)




   



