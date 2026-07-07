#Desafio 115
from time import sleep
from lib.interface import *
from lib.arquivo import *

arq = 'cadastro.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado!')
else:
    print('Arquivo Não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        #Opção de listar o conteudo do Arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nove pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('Erro! Digite uma Opção Válida!')




