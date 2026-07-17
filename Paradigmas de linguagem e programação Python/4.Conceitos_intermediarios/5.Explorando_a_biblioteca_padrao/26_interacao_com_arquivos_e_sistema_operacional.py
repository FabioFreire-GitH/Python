import os
from pathlib import Path
import shutil

print()
print(os.getcwd())
print(os.listdir())
pasta = 'POO'
os.chdir(pasta)
print(os.getcwd())
print(os.listdir())
print()
print(os.environ['PATH'])
print()
p = Path('.')
print(p.absolute())
print()
print(list(p.iterdir()))
print(list(path.absolute() for path in p.iterdir()))
print()
os.chdir('..')
print(os.listdir())
pasta_atual = Path(__file__).parent
nome_arquivo = 'notas.txt'
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_texto:
    arquivo_texto.write('Estou aprendendo Python')

shutil.move(nome_arquivo, pasta_atual / nome_arquivo)
os.chdir('Paradigmas de linguagem e programação Python')
os.chdir('4.Conceitos_intermediarios')
print(os.listdir('5.Explorando_a_biblioteca_padrao'))


