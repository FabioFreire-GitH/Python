from pathlib import Path
print()
#"Retornando" (Imprimindo) caminho de diretório de trabalho atual -> ate a pasta pai do projeto
print(Path.cwd())
print()

# Esse caminho é absoluto
print(Path.cwd().is_absolute())
print()

# Retornando caminho da pasta "Desafios" de Le_escrever_arquivos
print(Path('pasta_teste'))
print()

# Esse caminho é absoluto
print(Path('pasta_teste').is_absolute())
print()

# Transformando o caminho em absoluto
print(Path.cwd() / 'pasta_teste')
print((Path.cwd() / 'pasta_teste').exists()) # false porque a pasta Desafios esta dentro de outras pastas
print()
print(Path.cwd() / 'POO')
print((Path.cwd() / 'POO').exists()) # Essa ja é True
print()

# Garantindo que estamos retornando o caminho para a pasta do script
print(__file__)
print(Path(__file__).is_absolute())
print(Path(__file__).parent)
print(Path(__file__).parent / 'pasta_teste')
print((Path(__file__).parent / 'pasta_teste').is_absolute())
print()

# Trabalhando com partes de caminho
caminho_arquivo = Path(__file__) 
print(caminho_arquivo)
print(caminho_arquivo.anchor) # PAsta raiz... pasta do disco rigido
print(type(caminho_arquivo.parent))
print(caminho_arquivo.name)
print(caminho_arquivo.stem)
print(caminho_arquivo.suffix)
print(caminho_arquivo.drive) # nome do disco

print(caminho_arquivo.parent)
print(caminho_arquivo.parents[0])
print(caminho_arquivo.parents[1])
print(caminho_arquivo.parents[2])


