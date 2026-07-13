
valor_de_busca = 'xxx'
'''
resultado = buscar_no_banco_de_dados(valor_de_busca)
if resultado is None:
    print(f'Nada foi encontrado para o valor de busca "{valor_de_busca}".')
else:
    print(f'Resultados encontrados para valor de busca "{valor_de_busca}": {resultado}')


# Operador morsa (:=)

valor_de_busca = 'xxx'

if (resultado := buscar_no_banco_de_dados(valor_de_busca)) is None:
    print(f'Nada foi encontrado para o valor de busca "{valor_de_busca}".')
else:
    print(f'Resultados encontrados para valor de busca "{valor_de_busca}": {resultado}')
'''

# ---x---

# Sem operador morsa
n = 5
while n > 0:
    n -= 1
    print(n)

# Com operador morsa
n = 5
while (n := n-1) >= 0:
    print(n)