# Argumentos Arbitrários com *args e **kwargs

def somar(a,b):
    return a + b

resultado = somar(2,5) # se eu passar mais argumentos, retornoa um erro de TypeError
print(resultado) 
print()

# como resolver:
def novo_somar(*valores): #args 
    return sum(valores)

resultado = novo_somar(2,5,7,5,1,3,9)
print(resultado)
print()

def exibe_argumentos(*args, **kwargs): #args e kwargs (com nomes) 
    print(f'Argumentos passados sem palavra-chave: {args}')
    print(f'Argumentos passados com palavra-chave: {kwargs}')
    
exibe_argumentos(2, 5, 7, x=3, y=8)
print()

def exibe_argumentos(a, b, c, *args, **kwargs): #args e kwargs (com nomes) 
    print(a, b, c)
    print(f'Argumentos passados sem palavra-chave: {args}')
    print(f'Argumentos passados com palavra-chave: {kwargs}')
    
exibe_argumentos(2, 5, 7, 10, 50, x=3, y=8)
print()

def exibe_argumentos_2(*args, **kwargs): #args e kwargs (com nomes) 
    print(f'Argumentos passados sem palavra-chave: {args}')
    print(f'Argumentos passados com palavra-chave: {kwargs}')
    
valores = [1, 2, 4]
dic = {
    'nome': 'Fabio',
    'idade': 47,
}

#exibe_argumentos_2(valores, dicionario=dic)
#exibe_argumentos_2(*valores, dicionario=dic)
exibe_argumentos_2(*valores, **dic)