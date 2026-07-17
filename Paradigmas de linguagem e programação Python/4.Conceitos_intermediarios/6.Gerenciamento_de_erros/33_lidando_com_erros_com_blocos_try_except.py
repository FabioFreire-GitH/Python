'''
x = float(input('Digite um número: '))
y = float(input('Digite um divisor: '))

resultado = x / y
print(resultado)
'''
###
'''
try:
    x = float(input('Digite um número: '))
    y = float(input('Digite um divisor: '))
    resultado = x / y
    #print(resultado)
except:
    print('Erro')
else:
    print(resultado)
finally:
    print('Final do código')
'''
###
try:
    x = float(input('Digite um número: '))
except ValueError:
    x = 10
    print(f'Valor invalido para x, usando valor padrão {x}')

try:
    y = float(input('Digite um divisor: '))
except ValueError:
    y = 2
    print(f'Valor invalido para y, usando divisor padrão {x}')

try:
    resultado = x / y
except ZeroDivisionError:
    print(f'Impossível dividor {x} por {y}')
else:
    print(f'Resultado da divisão é {resultado}')
finally:
    print('Final do código')