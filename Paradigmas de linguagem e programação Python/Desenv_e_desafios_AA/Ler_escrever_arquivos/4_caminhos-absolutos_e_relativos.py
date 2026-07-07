'''
Na linguagem Python, caminhos são usados para localizar arquivos e diretórios no sistema de arquivos.
    Caminho Absoluto: É o endereço completo do arquivo ou pasta. Ele sempre começa a partir da raiz do disco (ex: / no Linux/macOS ou C:\ no Windows) e 
independe de onde o seu script está rodando.
    Caminho Relativo: É a localização do arquivo a partir do diretório onde o seu programa está sendo executado no momento. Geralmente começa com o nome 
da pasta ou com um ponto (.) para indicar a pasta atual.
'''
from pathlib import Path

caminho_projeto = Path()
print(caminho_projeto.absolute()) # porem para na pasta raiz do projeto
print()

caminho_arquivo = Path(__file__) # caminho ate o arquivo
print(caminho_arquivo)
print()

print(caminho_arquivo.parent) # pasta pai deste arquivo
print()

print(caminho_arquivo.parent.parent) # pasta pai do pai deste arquivo 
print()
