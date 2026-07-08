'''
print('Olá Mundo!') # aula 1 e 2
nome = input ('Digite seu nome: ')
print('Seu nome é: ', nome)
num1 = int(input ('Digite o primeiro numero: ')) # aula 3 e 4 Desafio que ficou para uma aula fututa (#6)
num2 = int(input ('Digite o segundo numeto: '))
soma = num1+num2
print('A soma é: ',soma)
msg = 'Olá, Mundo!' # aula 5
print(msg)
'''
# aula 6.1 - Tipos Primitivos
'''
num0 = input('Digite um numero: ')
print(type(num0))
'''
num1 = int(input ('Digite o primeiro numero: '))
num2 = int(input ('Digite o segundo numeto: '))
soma = num1+num2
#print('A soma é: ',soma)
#print('A soma entre', num1,'e',num2,'é:',soma)
print('A soma entre {} e {} é {}'.format(num1,num2,soma))

'''
exemplos de tipos Primitivos:
int (7, -4, 0, 9875) - inteiros
float (4.5, 0.076, -15.226, 7.0) - real ou flutuante
bool (True, False) - booleanos - OBS: sempre com a primeira letra maiuscula
str ('Olá', '7,5', '') - string - OBS: sempre entre aspas, simples'' ou duplas"". Vazio tambem é uma string
* Juntar uma string na outra é contatenar e usa o +
'''
'''
O print possui uma outra forma de sintaxe:
a primeira : print('A soma é: ', soma)
a outra forma é: print('A soma é: {}', format(soma))
'''

# aula 6.2 - Tipos Primitivos
print()#pular linha
print('Testando o float')
n = float(input('Digite um valor: '))
print(n)
print()#pular linha
print('Testando o booleano')
n = bool(input('Digite um valor: ')) # Aqui pergunta: Tem valor dentro da variavel se sim True, se vazio False
print(n)
print()#pular linha
print('Testando string')
n = input('Digite um valor: ')
print(n)
print()#pular linha
print('Verificando se o valor digitado como string é um numero')
n = input('Digite um valor ou algo: ')
print(n.isnumeric())#verifica se é possivel converter o conteudo em num tipo int
print()#pular linha
print(n)
print('Verificando se o valor digitado como string é um letra')
print(n.isalpha())#verifica se é possivel converter o conteudo em num tipo alpha (de alfabetico, ou seja LETRA)
print()#pular linha
print('Verificando se o valor digitado como string é um alphanumerico')
n = input('Digite um valor ou algo: ')
print(n.isalnum())#verifica se o conteudo é alphanumerico
print()#pular linha
