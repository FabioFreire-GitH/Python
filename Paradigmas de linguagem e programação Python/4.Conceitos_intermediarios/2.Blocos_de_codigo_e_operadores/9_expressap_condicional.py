x = 4
y = 5
if x > y:
    maior_valor = x
else:
    maior_valor = y
print(maior_valor)

'''
Operadores ternários
Em linguagens de programação, operadores ternários tem a seguinte estrutura:
VAR = CONDIÇÃO ? VALOR SE VERDADEIRO ; VALOR SE FALSO
Essa estrutura é altamente utilizada, desde a linguagem C até a função SE= do Excel!
'''
'''
Expressões condicionais: operadores ternários em Python
VAR = VALOR_VERDADEIRO SE CONDIÇÃO SENÃO VALOR_FALSO
'''
maior_valor = x if x > y else y
print(maior_valor)

def pegar_cor(valor):
    return 'vermelho' if valor < 0 else 'azul'

for valor in [-1,0,1]:
    print(f'A cor do valor {valor} é {pegar_cor(valor)}')

numeros = [1,2,3,4]

pares_quadrados = [
    n ** 2
    #if n % 2 == 0
    #else n
    for n in numeros
]
print(pares_quadrados)

