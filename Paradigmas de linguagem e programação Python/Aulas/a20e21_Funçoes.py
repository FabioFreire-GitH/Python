# Aula 20 e 21: FUNÇÕES
#Explicaçoes do Guanabara

# Funçao está intimamente ligada a Rotina
# def = definiçao de funçao personalizada

#EXEMPLO 1:
def lin():
    print('-'*30)


lin()
print('CURSO EM VIDEO')
lin()
print()

#EXEMPLO 2:
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


mensagem('CURSO EM VIDEO')
print()

#PRATICA 1
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A e B = {s}')


#Programa Principal
soma(4, 5)
soma(a=4, b=5)#
soma(b=4, a=5)# se for explicitar, deve explicitar todos os termos
print()

# Funcionalidade empacotamento
# serve como contador 
# ex.: def contador(*num): # o asteristico é o simbolo de DESEMPACOTAR. Significa para o PYTHON que podem vir varios parametros. diferentemente da pratica acima que sao somente 2.

#PRATICA 2
def contador(*num):
    for v in num:
        print(f'{v} ', end='')
    print('Fim...')
    tam =len(num)
    print(f'Tamanho = {tam}')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print()

#PRATICA 3
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
print()

#PRATICA 4
def soma2(*valores):
    s = 0
    for n in valores:
        s += n
    print(f'Somando os valores {valores} temos {s}.')


soma2(5, 2)
soma2(2, 9, 4)
print()
# Em cada situação, é melhor usar o desempacotamente e outros a lista.


##AULA 20 - FUNÇOES PARTE 2

## Interactive Help 
## docstrings (forma de documentação)
## Argumentos opcionais: util, importante e valioso
## Escopo de variáveis
## Retorno de resultados


### Interactive Help (Ajuda Interativa) ###
# Comoando: help() -> na verdade um comando interno pois abre e fecha parenteses que se chama Função. Um método.
# Digite python no terminal e depois help() --- quit() para sair
# pode fazer desta forma tambem:
help(print)
#outra forma é imprimir o documento interno
print(input.__doc__)
print('-='*30)

### Dosctrings ###

def contador (i, f, p):
    """
    descriçao da função   
    """
    for v in range(i, f, p):
        print(f'[{v}] ', end='')

contador(2, 10 ,2)
help(contador)

#PARAMETROS OPCIONAIS
def somar(a=0,b=0,c=0):
    s =a+b+c
    print(f'Soma = {s}')


somar(3,2,5)
somar(8,4) # aqui esta o problema, caso nao ponha o parametro opcional em c (c=0) dá erro. Com o parametro vai funconar caso nao tenha um terceiro paramebro para chamada da função

#podemo colocar o parametro = 0 para todos. def somar(a=0,b=0,c=0)
somar()
print()
### Escopos de variaveis ###


# Abaixo um exemplo de Escopo Global - a variavel n declarada no programa principal, na chamada da funçao funciona em todo esse condigo

def test():
    print(f'Na função teste, n vale {n}')


#Programa principal
n = 2
print(f'No programa principal, n vale {n}')
test()
print()

# Abaixo um exemplo de Escopo Local - A variavel x só funciona na função

def test():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa principal
n = 2
print(f'No programa principal, n vale {n}')
test()
#print(f'No programa principal, x vale {x}')# aqui nao funcioa, dá erro
print()

#Exemplo 2
def teste(b):
    b += 4
    c = 2
    # caso declare uma variavel a, o Python cria uma variavel a Local 
    a = 8
    print(f'A dentro da função vale {a}') # a - Escopo Global funciona em todo programa - Inclusive dentro da funçao - Porem declarando 'a'  dentro da função o python cria essa variavel tamebm de forma Local
    print(f'B dentro da função vale {b}') # Variavel de Escopo Local - Só funciona dentro desta função
    print(f'C dentro da função vale {c}') #Variavel de Escopo Local - Só funciona dentro desta função


a = 5 # Variavel de Escopo Glogal
teste(a)
print(f'A fora da função vale {a}')
print()

#Exemplo 3
def teste2(b):
    global a # Essa forma, eu informou ao program nao criar uma variavel local e sim utilizar a Global
    b += 4
    c = 2
    a = 8 # altera a variavel de forma Global
    print(f'"a" dentro da função vale {a}') # Variavel Global dentro da funçao
    print(f'"b" dentro da função vale {b}') # Variavel de Escopo Local - Só funciona dentro desta função
    print(f'"c" dentro da função vale {c}') #Variavel de Escopo Local - Só funciona dentro desta função


a = 5 # Variavel de Escopo Glogal
print(f'"a" fora antes da chamada da função vale {a}')
teste2(a)
print(f'"a" fora após a chamada da função vale {a}')
print()


### RETORNO DE VALORE ###
# comando: return

#aqui nao dá para mostra exemplo: As somas valem 10, 4 e 6
def somar(a=0,b=0,c=0):
    s =a+b+c
    print(f'Soma = {s}')


somar(3,2,5)
somar(2, 2)
somar(6)
print()


#Abaixo retorna uma valor usando o return
def somar(a=0,b=0,c=0):
    s =a+b+c
    return s


#print(somar(3,2,5))
r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)
print(f'Meus cálculos deram: {r1}, {r2} e {r3}')
print()


### PRATICA EXERCICIO 1 ###
# Calcular o fatorial de um numero e restornar ao programa principal

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c 
    return f


n = int(input('Digite um numero:'))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print()

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
n = int(input('Digite um numero: '))
print(par(n))
