from pathlib import Path

# Lendo um arquivo forma não recomendada
'''
pasta_atual  = Path(__file__).parent
lista_compras = open(pasta_atual / 'lista_de_compras.txt')
print(lista_compras.read())
lista_compras.close()
'''

# Lendo arquivo forma recomendada
'''
pasta_atual  = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt', mode='r', encoding= 'utf-8' ) as lista_compras: # o mode = 'r' é padrao caso nao expecifique
    print(lista_compras.read()) # Maior vantagem nao precisa fechar
'''
    
# Lendo linha a linha
'''
pasta_atual  = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt', mode='r', encoding= 'utf-8' ) as lista_compras: # o mode = 'r' é padrao caso nao expecifique
    linha = lista_compras.readline()
    while linha !='':
        print(linha)
        linha = lista_compras.readline()
'''
        
# Lendo todas as linhas
'''
pasta_atual  = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt', mode='r', encoding= 'utf-8' ) as lista_compras:
    print(lista_compras.readlines())
'''

# Escrevendo arquivo
'''
pasta_atual  = Path(__file__).parent
itens_ja_comprados = ['Arroz','Feijão','Tomate']

with open(pasta_atual / 'lista_de_compras.txt', encoding='utf-8') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w', encoding='utf-8') as lista_atualizada:
    for item in itens_lista:
        if not item.replace('\n','') in itens_ja_comprados:
            lista_atualizada.write(item)
'''

# Escrevendo linha a linha
'''
pasta_atual  = Path(__file__).parent
itens_ja_comprados = ['Arroz','Feijão','Tomate']

with open(pasta_atual / 'lista_de_compras.txt', encoding='utf-8') as lista_compras:
    itens_lista = lista_compras.readlines()

itens_lista_atualizada = []
for item in itens_lista:
    if item not in itens_ja_comprados:
        itens_lista_atualizada.append(item )

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w', encoding='utf-8') as lista_atualizada:
    lista_atualizada.writelines(itens_lista_atualizada)
'''

# Acrescentando valores a um arquivo

pasta_atual = Path(__file__).parent

novos_itens = ['banana']
novos_itens_c_quebra = [f'\n{item}' for item in novos_itens]

with open (pasta_atual / 'lista_de_compras.txt', mode= 'a', encoding= 'utf-8') as lista_adicionada:
    lista_adicionada.writelines(novos_itens_c_quebra)


