from pathlib import Path
import shutil

# Criando pasta
'''
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino4'
caminho_pasta_destino.mkdir(exist_ok=True)
'''

# Criando pasta com todas as pastas antediores necessárias
'''
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino5' / 'destino5.1'
caminho_pasta_destino.mkdir(parents=True)# sem a flag parents=true nao cria pasta que nao existe com a subpasta
'''

# Copiando pastas
'''
pasta_atual = Path(__file__).parent
shutil.copytree(pasta_atual / 'destino5', pasta_atual / 'destino1' / 'destino5')
'''

# Deletendo pastas vazias
'''
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino5' / 'destino5.1'
pasta_remover.rmdir() # so delat pastas VAZIA
'''

# Deletando pastas com conteúdo
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino1' 
shutil.rmtree(pasta_remover)






