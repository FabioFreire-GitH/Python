from pathlib import Path

caminho = Path('pasta_teste/pasta-exerc-3') # ou caminho = Path('Desafios) / Path('pasta-exerc-3') // afim de evitar erros usar caminhos completos desde o C: (para o windows lembrar de por \\)

for arq in ['teste1.txt','teste2.txt','teste3.txt']:
    caminho_arquivo = caminho / arq # a primeira variavel (caminho) seja uma Path
    print(caminho_arquivo)


#################
print(Path.home())

print(Path.home() / 'Documents' / 'assim-por-diante')