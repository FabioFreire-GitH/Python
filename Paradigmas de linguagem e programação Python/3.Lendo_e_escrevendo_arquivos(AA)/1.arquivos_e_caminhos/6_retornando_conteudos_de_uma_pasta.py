from pathlib import Path
import os

# Listando arquivos de uma pasta
print(os.listdir(Path.home()))
print()
print(Path.cwd().glob('*'))
print()
print(list(Path.cwd().glob('*')))
print()

# Listando arquivos de uma determinada Extensão
print(list(Path.cwd().glob('*.md')))
print()

# Listar tudo dentro de uma pasta
#print(list(Path.cwd().glob('**/*'))) #Pega tudo
print(list(Path.cwd().glob('**/*.txt')))
print()

# Validando caminhos
print(Path.home().exists())
print()

# Verificando se é arquivo ou pasta
print(Path(__file__))
print(Path(__file__).is_file())
print()

print(Path(__file__).parent)
print(Path(__file__).parent.is_file())
print()

print(Path(__file__).parent)
print(Path(__file__).parent.is_dir())
print()

print(Path(__file__))
print(Path(__file__).is_dir())
print()

