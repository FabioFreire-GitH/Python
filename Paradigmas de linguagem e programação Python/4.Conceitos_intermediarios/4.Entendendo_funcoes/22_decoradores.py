def func():
    return 2

minha_funcao = func
retorno = minha_funcao()
print(retorno)
print()

def exibe_func(f):
    print(f'Objeto de função recebido: {f}')
    print(f'Nome da função: "{f.__name__}"')

exibe_func(func) # lembrando e reparando qeu nao estou chamando a função com () somente o objeto funçao
print()

def func_externa(x):

    def func_interna():
        return x + 2
    
    valor = func_interna()
    return valor


resultado = func_externa(3)
print(resultado)
print()

def pega_func_interna(x):
    def func_interna(y):
        return x + y + 2
    return func_interna

f = pega_func_interna(1)
resultado = f(2)
print(resultado)
print()

###############################
from meus_decoradores import fazer_duas_vezes, medir_tempo
import time

print('#'*30)
print('DECORADORES - aula 22')
print('#'*30)
print()

@fazer_duas_vezes
def printar_exclamações():
    print('!!!')

printar_exclamações()
print()

@medir_tempo
def dizer_oi(nome):
    time.sleep(1)
    return f'Olá, {nome}!'

resultado = dizer_oi("Juliano")
print(resultado)

print()
print('#'*30)
print('DECORADORES - aula 23')
print('#'*30)
print()



def meu_decorador(func):
    def meu_pacote(*args, **kwargs):
        retorno = func(*args, **kwargs)
        return retorno.upper()
    return meu_pacote

def dizer_oi(nome):
    return f'Olá, {nome}!'

print(dizer_oi('Fábio'))

@meu_decorador
def dizer_oi(nome):
    return f'Olá, {nome}!'

#dizer_oi= meu_decorador(func=dizer_oi)

print(dizer_oi('Fábio'))