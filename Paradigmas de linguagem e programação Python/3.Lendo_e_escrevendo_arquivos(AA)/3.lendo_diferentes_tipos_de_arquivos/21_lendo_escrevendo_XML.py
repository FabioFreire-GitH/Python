import xml.dom.minidom
from pathlib import Path

# Lendo arquivo xml
pasta_atual = Path(__file__).parent
domtree = xml.dom.minidom.parse(str(pasta_atual / 'xmls' / 'livros.xml')) # aqui precisa passar como string e nao como path
#print(domtree)

group = domtree.documentElement
#print(group)
livros = group.getElementsByTagName('livro')
#print(livros)
#print(len(livros))

# Interando por elementos e retornando valores
for livro in livros:
    titulo = livro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
    autor = livro.getElementsByTagName('autor')[0].childNodes[0].nodeValue
    print('Título: ', titulo, '| Autor: ', autor)


# Salvando um arquivo xml
livros[0].getElementsByTagName('autor')[0].childNodes[0].nodeValue = 'Fabio Freire'

with open(pasta_atual / 'xmls' / 'livros_copia.xml', 'w') as f:
    domtree.writexml(f)