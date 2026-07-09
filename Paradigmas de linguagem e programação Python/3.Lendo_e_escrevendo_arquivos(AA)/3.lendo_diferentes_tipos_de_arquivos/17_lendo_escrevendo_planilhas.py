from pathlib import Path
import pandas as pd # Uma 'alias' em convençao de programadores para pandas, devido a uma grande utilização deta biblioteca

pasta_atual = Path(__file__).parent

# Lendo tabelas com DataFrame
'''
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx')
print(tabela_clientes.head(10))
'''

# Lendo aba especifica
''' 
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SP')
print(tabela_clientes.head(10))
'''

# modificando header
'''
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SP')
print(tabela_clientes.head(10))
print()

tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SP', header=1)
print(tabela_clientes.head(10))
print()

tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SP', header=0, index_col=0)
print(tabela_clientes.head(10))
print()
'''

# Adicionado coluna de index
'''
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SP', index_col=0)
print(tabela_clientes.head(10))
'''

# Lendo Colunas especificas
'''
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SP', usecols="A:B") # ou usecols =[0, 1] -> pega a coluna 0 e 1 
print(tabela_clientes.head(10))
'''

# Comentarios sobre decimais e thousands
'''
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', decimal='.')
print(tabela_clientes.head(10))

tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', thousands='.')
print(tabela_clientes.head(10))
'''

# Escrevndo planilha
'''
tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', index_col=0)
tabela_clientes.to_excel(pasta_atual / 'planilhas'/ 'copia_clientes2.xlsx')
'''

# Escrevendo diversos abas
tabela_clientes_RJ = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='RJ')
tabela_clientes_SP = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name='SP')

with pd.ExcelWriter(pasta_atual / 'planilhas'/ 'copia_clientes3.xlsx') as nova_planilha:
    tabela_clientes_RJ.to_excel(nova_planilha, sheet_name='RJ',index=False)
    tabela_clientes_SP.to_excel(nova_planilha, sheet_name='SP')