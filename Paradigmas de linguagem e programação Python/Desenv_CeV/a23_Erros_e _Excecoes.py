# Aula 23: ERROS E EXCEÇÕES
#Explicaçoes do Guanabara

#Comand:
'''
try:
    "operação"
except:
    "Falhou"
'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except:
    print('Erro...')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!!')


print()

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'O problema foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!!')

    print()

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possuivel dividir um numéro por Zero.')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados.')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!!')