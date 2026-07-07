# Aula 18: LISTAS (Variaveis Compostas) PARTE 2 - usa Colchetes []
# AS LISTAS SÃO MUTAVEIS. 

# Lista dentro de lista

print('-='*30)
print('{:^60}'.format('EXEMPLIFICAÇÕES'))
print('-='*30)
dados = ['Pedro',25,'Maria',19,'João',32] # indices de dados 0 = pedro; 1 = 25; maria = 2 ...

#lista que contem a lista acima
#pessoas.append(dados[:])
pessoas = [['Pedro',25],['Maria',19],['João',32]] # Indices de pessoas pedro e 25 = 0 e etc. Chamada Estrutura -- Lista dentro de lista

print(pessoas[0][0]) #Print de pessoas 0, elemento 0. 'Pedro'
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1]) # ['Maria',19]
print()


print('-='*30)
print('{:^60}'.format('PARTE PRÁTICA - 1 '))
print('-='*30)
#Parte Pratica

teste = list()
teste.append('Fabio')
teste.append(47)
print(teste)
galera = list()
galera.append(teste[:])#se nao por o [:] vai criar uma ligação
teste[0] = 'Suelem'
teste[1] = 44
galera.append(teste[:])
print(teste)
print(galera)
print()

print('-='*30)
print('{:^60}'.format('PARTE PRÁTICA - 2 '))
print('-='*30)
#da para criar assim : 
galera = [['Pedro',25],['Maria',19],['João',32]]
for p in galera:
    print(p)
    print(f'{p[0]} tem {p[1]} anos de idade.')
print()


print('-='*30)
print('{:^60}'.format('PARTE PRÁTICA - 3 '))
print('-='*30)
grupo = list()
dado = list() # Estrutua auxiliar
totmaior = totmenor = 0
for c in range(0,4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    grupo.append(dado[:])
    dado.clear()
for p in grupo:
    if p[1] >= 21:
        print(f'\n{p[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'\n{p[0]} é menor de idade!') 
        totmenor += 1
print(f'\nTemos {totmaior} maiores e {totmenor} menores de idade!\n')
print('Dados limpos: ', dado)
print(grupo)
print('\nFim...\n')