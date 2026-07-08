from pathlib import Path
import shutil
import os

# Copiando arquivo com copyfile
  # Duas bibliotecas uteis para se copiar arquivos:  os e shutil
  # O modulo shutil foi construido sobre o modulo os, entao ela tb utiliza o mudulo os
  # O shutil é mais eficiente e confiavel
  # desvantagem: Quando utiliza o copyfile ele nao copia as permissoes do arquivo origem, ou seja, se só um administrador puder abrir o texto original, essa perissoes nao irão na copia.
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino1' / 'texto.txt'

shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)
'''

# Copiando arquivo com copy - a diferença que nao usamos o nime do arquivo no destino, somente a pasta.
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino2'

shutil.copy(caminho_arquivo, caminho_pasta_destino)
'''

# Copiando arquivo com copy2 - alem do arquivo, tambem é copiado os meta dados desse arquivo (quando o arquivo foi criado, por quem, etc)
''' 
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino3'

shutil.copy2(caminho_arquivo, caminho_pasta_destino)
'''

# Movendo arquivos - pode usar como o destino pasta ou destino com o nome do arquivo = caminho_arquivo_destino = pasta_atual / 'destino1' / 'texto.txt'
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino1'

shutil.move(caminho_arquivo, caminho_pasta_destino)
'''

# Deletando arquivos - importar o modulo os
 # vamos copiar o arquivo primeiro para a pasta destino3 e depois deletar o original

pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino3' / 'texto.txt'

shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)
if caminho_arquivo.exists():
    os.remove(caminho_arquivo)


